from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import uuid


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        _("name"),
        max_length=200,
        help_text=_("Enter a book genre (e.g. Science Fiction)")
    )

    def __str__(self) -> str:
        """String representing the Model object."""
        return self.name

    def __repr__(self) -> str:
        """unambiguous string representation -
        meant for developers and debugging purposes"""
        return (
            f"{self.__class__.__name__} class, "
            f"(id={self.id}, name={self.name})"
        )


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)"""
    title = models.CharField(
        _("title"),
        max_length=200,
    )
    # foreign key, one author -> many books
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("author")
    )
    summary = models.TextField(
        _("summary"),
        max_length=1000,
        help_text=_("Enter a brief description of the book")
    )
    isbn = models.CharField(
        _("ISBN"),
        max_length=13,
        unique=True,
        help_text=_(
            '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'  # noqa
            )
    )
    # Many to Many relations bc genre can cover many books, and many books can
    # have same generes
    genre = models.ManyToManyField(
        Genre,
        help_text=_("Select a genre for this book"),
        verbose_name=_("genre")
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("language"),
    )

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        """String representing the Model object"""
        return (
            self.title if not self.author
            else f"{self.title} by {self.author.first_name[0]}.{self.author.last_name}"  # noqa
        )

    def __repr__(self):
        """unambiguous string representation -
        meant for developers and debugging purposes"""
        return (
            f"{self.__class__.__name__} class, "
            f"(id={self.id}, title={self.title} "
            f"author='{self.author}', isbn='{self.isbn})"
        )

    def get_absolute_url(self):  # to see the view on site button
        """Returns the URL to access a detail record for this book."""
        return reverse('app_catalog:book-detail', kwargs={'pk': self.pk})


class BookInstance(models.Model):
    """Model representing a specific copy of a book
    (i.e.) that can be borrowed from the library."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Unique ID for this particular book across whole library")
    )
    # realtionship one book -> many bookInstances
    book = models.ForeignKey(
        'Book',
        on_delete=models.RESTRICT,
        null=True,
        verbose_name=_("book")
    )
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("borrower")
    )
    imprint = models.CharField(
        _("imprint"),
        max_length=200
    )
    due_back = models.DateField(
        _("Due back"),
        null=True,
        blank=True,
        help_text=_("Enter the due date for this item")
    )

    LOAN_STATUS = (
        ('m', _('Maintenance')),
        ('o', _('On loan')),
        ('a', _('Available')),
        ('r', _('Reserved')),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default=LOAN_STATUS[0][0],
        help_text=_("Book availability"),
    )

    class Meta:
        ordering = ['due_back']
        permissions = [
            ("can_mark_returned", "Can Set book as returned"),
            ("can_renew", "Can extend the book return date"),
            ("can_view_staff", "Can see the staff view"),
        ]

    def __str__(self) -> str:
        """String for representing the Model object."""
        return f"{self.id} ({self.book.title})"

    def __repr__(self):
        """unambiguous string representation -
        meant for developers and debugging purposes"""
        return (
            f"{self.__class__.__name__} class, "
            f"(id={self.id}, book={self.book}, "
            f"status={self.get_status_display()}"
            f"due_back={self.due_back}"
        )

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on
        the due date and current date"""
        # print(self.due_back.date(),timezone.now().date())
        return self.due_back and self.due_back < timezone.now().date()


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(
        _("first name"),
        max_length=100
    )
    last_name = models.CharField(
        _("last name"),
        max_length=100
    )
    date_of_birth = models.DateField(
        _("Date of birth"),
        null=True,
        blank=True,
    )
    date_of_death = models.DateField(
        _("Date of death"),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self) -> str:
        """String for representing the Model object"""
        return f"{self.first_name}, {self.last_name}"

    def __repr__(self):
        """unambiguous string representation -
        meant for developers and debugging purposes"""
        return (
            f"{self.__class__.__name__} class, "
            f"(id={self.id}, first_name={self.first_name},"
            f"last_name={self.last_name}"
            f"date_of_birth='{self.date_of_birth}', date_of_death='{self.date_of_death})" # noqa
        )

    def get_absolute_url(self):  # to see the view on site button
        """Returns the URL to access a particular author instance."""
        return reverse('app_catalog:author-detail', kwargs={'pk': self.pk})

    def clean(self) -> None:
        """checking if the date of birth is before the date of birth"""
        # parent class clean method logic
        super().clean()
        # cusotm logic
        if self.date_of_birth and self.date_of_death:
            if self.date_of_death < self.date_of_birth:
                raise ValidationError("Date of death must be after the date of birth.")  # noqa


class Language(models.Model):
    """Model representing a Language (English, French etc.)."""
    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Enter the language of the book")
    )

    def __str__(self) -> str:
        """String for representing the Model object"""
        return self.name

    def __repr__(self):
        """unambiguous string representation -
        meant for developers and debugging purposes"""
        return (
            f"{self.__class__.__name__} class, "
            f"(id={self.id}, name={self.name},"
        )
