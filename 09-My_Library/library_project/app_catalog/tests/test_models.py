"""
Test for models form the app catalog
"""
from app_catalog.models import Book, BookInstance, Author, Genre, Language
from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from unittest.mock import patch, MagicMock
import uuid


class BookModelTestCase(TestCase):
    """Test cases for the Book model"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        cls.genre = Genre.objects.create(name='Fiction')
        cls.language = Language.objects.create(name="English")
        cls.book = Book.objects.create(
            title='Test Book',
            author=cls.author,
            summary='This is a test book summary.',
            isbn='1234567123012',
            language=cls.language
        )
        cls.book.genre.add(cls.genre)

    def test_book_fields(self):
        """Testing the book object in the database"""
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.summary, 'This is a test book summary.')
        self.assertEqual(book.isbn, '1234567123012')
        self.assertEqual(book.language, self.language)
        # check the many-to-many relationship with Genre
        genres = book.genre.all()
        expected_genre_names = ['Fiction']
        actual_genre_names = [genre.name for genre in genres]
        self.assertEqual(len(genres), len(expected_genre_names))
        self.assertEqual(actual_genre_names, expected_genre_names)

    def test_book_str_representation(self):
        """Testing the book object str representation"""
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(str(book), f'Test Book by {book.author.first_name[0]}.{book.author.last_name}')  # noqa
        expected_repd = (
            f"Book class, "
            f"(id={book.id}, title={book.title} "
            f"author='{book.author}', isbn='{book.isbn})"
        )
        self.assertEqual(repr(book), expected_repd)


class GenreModelTestCase(TestCase):
    """Test cases for the Genre model"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.genre_name = "Science Fiction"
        cls.genre = Genre.objects.create(name=cls.genre_name)

    def test_genre_fields(self):
        """Testing the genre model fields"""
        genre = Genre.objects.get(id=self.genre.id)
        self.assertEqual(genre.name, self.genre_name)

    def test_genre_str_representation(self):
        """Testing the genre object str representation"""
        genre = Genre.objects.get(id=self.genre.id)
        self.assertEqual(str(genre), self.genre_name)
        expected_repd = (
            f"Genre class, "
            f"(id={genre.id}, name={genre.name})"
        )
        self.assertEqual(repr(genre), expected_repd)


class LanguageModelTestCase(TestCase):
    """Test cases for the Language model"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.language_name = "English"
        cls.language = Language.objects.create(name=cls.language_name)

    def test_language_fields(self):
        """Testing the Language model fields"""
        language = Language.objects.get(id=self.language.id)
        self.assertEqual(language.name, self.language_name)

    def test_language_str_representation(self):
        """Testing the language object str representation"""
        language = Language.objects.get(id=self.language.id)
        self.assertEqual(str(language), self.language_name)
        expected_repr = (
            f"Language class, "
            f"(id={language.id}, name={language.name},"
        )
        self.assertEqual(repr(language), expected_repr)


class AuthorModelTestCase(TestCase):
    """Test cases for the Author model"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 1, 1),
            date_of_death=date(2020, 12, 31)
        )

    def test_author_fields_exists(self):
        """Testing the Author model fields exists"""
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(self.author.first_name, author.first_name)
        self.assertEqual(self.author.last_name, author.last_name)
        self.assertEqual(self.author.date_of_birth, author.date_of_birth)
        self.assertEqual(self.author.date_of_death, author.date_of_death)

    def test_author_str_representation(self):
        """Testing the Author object str representation"""
        author = Author.objects.get(id=self.author.id)
        self.assertEqual(str(author), f"{author.first_name}, {author.last_name}")  # noqa
        expected_repr = (
            f"Author class, "
            f"(id={author.id}, first_name={author.first_name},"
            f"last_name={author.last_name}"
            f"date_of_birth='{author.date_of_birth}', date_of_death='{author.date_of_death})" # noqa
        )
        self.assertEqual(repr(author), expected_repr)

    def test_null_dates_birth_death(self):
        """Testing if dataes not set are defaulted to null"""
        author = Author.objects.create(first_name="Null", last_name="Date")
        self.assertIsNone(author.date_of_birth)
        self.assertIsNone(author.date_of_death)

    def test_ordering(self):
        """Testing if ordering of the authors works last_name, fist_name"""
        author_1 = Author.objects.create(first_name="Alice", last_name="Smith")
        author_2 = Author.objects.create(first_name="Bob", last_name="Smith")
        author_3 = Author.objects.create(first_name="Eve", last_name="Brown")
        authors = Author.objects.all()
        self.assertEqual(
            list(authors),
            [author_3, self.author, author_1, author_2]
        )

    def test_date_of_birth_before_date_of_death(self):
        """Testing the date of birth before date of death"""
        author = Author(
            first_name="Invalid",
            last_name="Dates",
            date_of_birth=date(1990, 1, 1),
            date_of_death=date(1980, 12, 31)
        )
        with self.assertRaises(ValidationError):
            author.clean()

    def test_first_name_max_length(self):
        """testing the max length of first name"""
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        """testing the max length of last name"""
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_get_absolute_url(self):
        """testing the method for returning the aboslute url"""
        author = Author.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1/')


class BookInstaceModelTestCase(TestCase):
    """Test cases for the BookInstace model"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = Author.objects.create(first_name="John", last_name="Doe")
        cls.genre = Genre.objects.create(name="Mystery")
        cls.language = Language.objects.create(name="English")
        cls.book = Book.objects.create(
            title="Sample book",
            author=cls.author,
            summary="A sample book fro testing",
            isbn="12433551245",
            language=cls.language
        )
        cls.book.genre.add(cls.genre)
        cls.my_id = uuid.uuid4()
        cls.today = date.today()
        cls.yesterday = cls.today - timedelta(days=1)
        cls.tomorrow = cls.today + timedelta(days=1)
        cls.book_instance = BookInstance.objects.create(
            id=cls.my_id,
            book=cls.book,
            imprint="Sample Imprint",
            due_back=cls.today,
            status='a'
        )
        cls.curent_timezone = timezone.get_current_timezone()

    def test_book_instance_fields(self):
        """Testing fields of book instace"""
        book_instance = BookInstance.objects.get(id=self.my_id)
        self.assertEqual(book_instance.book, self.book)
        self.assertEqual(book_instance.imprint, "Sample Imprint")
        self.assertEqual(book_instance.due_back, self.today)
        self.assertEqual(book_instance.status, 'a')

    def test_book_instance_str_representation(self):
        """Testing the book_instance object str representation"""
        book_instance = BookInstance.objects.get(id=self.my_id)
        self.assertEqual(str(book_instance), f"{book_instance.id} ({book_instance.book.title})")  # noqa
        expected_repr = (
            f"BookInstance class, "
            f"(id={book_instance.id}, book={book_instance.book}, "
            f"status={book_instance.get_status_display()}"
            f"due_back={book_instance.due_back}"
        )
        self.assertEqual(repr(book_instance), expected_repr)

    def test_due_date_ordering(self):
        """Testing the ordering of the book_instances"""
        book_instance_yesterda = BookInstance.objects.create(
            book=self.book,
            imprint="Sample Imprint 2",
            due_back=self.yesterday,
            status='a'
        )
        book_instance_tomorrow = BookInstance.objects.create(
            book=self.book,
            imprint="Sample Imprint 3",
            due_back=self.tomorrow,
            status='a'
        )
        all_book_instances = BookInstance.objects.all()
        self.assertEqual(
            list(all_book_instances),
            [
                book_instance_yesterda,
                self.book_instance,
                book_instance_tomorrow
            ]
        )

    @patch('app_catalog.models.timezone.now')
    def test_is_overdue_with_overdue_date(self, mock_now: MagicMock):
        """Testing is_overdue property with an overdue due date"""
        self.book_instace_overdue_1 = BookInstance.objects.create(
            due_back=date(2023, 1, 18),
            imprint="book1"
        )
        self.book_instace_overdue_2 = BookInstance.objects.create(
            due_back=date(2023, 1, 19),
            imprint="Book2"
        )

        mock_now.return_value = timezone.datetime(
            2023, 1, 20,
            tzinfo=self.curent_timezone
        )
        self.assertTrue(self.book_instace_overdue_1.is_overdue)
        self.assertTrue(self.book_instace_overdue_2.is_overdue)

    @patch('app_catalog.models.timezone.now')
    def test_is_overdue_with_not_overdue_date(self, mock_now: MagicMock):
        """Testing is_overdue property with an not overdue due date"""
        self.book_instace_overdue = BookInstance.objects.create(
            due_back=date(2023, 1, 22),
            imprint="book1"
        )

        mock_now.return_value = timezone.datetime(
            2023, 1, 20,
            tzinfo=self.curent_timezone
        )
        self.assertFalse(self.book_instace_overdue.is_overdue)

    @patch('app_catalog.models.timezone.now')
    def test_is_overdue_with_empty_date(self, mock_now: MagicMock):
        """Testing is_overdue property with empty overdue due date"""
        self.book_instace_overdue = BookInstance.objects.create(
            imprint="book1"
        )

        mock_now.return_value = timezone.datetime(
            2023, 1, 20,
            tzinfo=self.curent_timezone
        )
        self.assertFalse(self.book_instace_overdue.is_overdue)
