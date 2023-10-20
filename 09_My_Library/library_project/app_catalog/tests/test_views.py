from app_catalog.models import Author, Book, BookInstance
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta


class IndexViewTest(TestCase):
    """Testing the index view"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        num_test_books = 10
        for i in range(num_test_books):
            author = Author.objects.create(
                first_name=f"First name {i}",
                last_name=f"Last name {i}"
            )
            Book.objects.create(
                title=f"Test Book {i}",
                isbn={i},
                author=author
            )

    def test_index_view_data(self):
        """Testing the data is send in the index page"""
        res = self.client.get(reverse('app_catalog:index'))
        self.assertEqual(res.status_code, 200)
        self.assertIn('num_books', res.context)
        self.assertIn('num_instances', res.context)
        self.assertIn('num_instaces_available', res.context)
        self.assertIn('num_authors', res.context)
        self.assertIn('num_genres', res.context)
        self.assertIn('current_year', res.context)

    def test_num_visits_in_sesions(self):
        """Testing the num visits if stored corectly in the session"""
        session = self.client.session
        session['num_visits'] = 0
        session.save()
        res = self.client.get(reverse('app_catalog:index'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "You have visited this page 0 times.")

        res = self.client.get(reverse('app_catalog:index'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "You have visited this page 1 time.")

        updated_session = self.client.session
        self.assertEqual(updated_session['num_visits'], 2)


class BookListViewTest(TestCase):
    """Testing Book list view"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        num_test_books = 10
        for i in range(num_test_books):
            author = Author.objects.create(
                first_name=f"First name {i}",
                last_name=f"Last name {i}"
            )
            Book.objects.create(
                title=f"Test Book {i}",
                isbn={i},
                author=author
            )

    def test_list_books_view(self):
        """Testing the books are retrived corectly"""
        res = self.client.get(reverse('app_catalog:books'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'app_catalog/book_list.html')
        self.assertTrue(len(res.context['book_list']) > 0)

    def test_pagination_books_view(self):
        """Testing pagination for the books view"""
        res = self.client.get(reverse('app_catalog:books'))
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(res.context['book_list']) == 5)

        res = self.client.get(reverse('app_catalog:books')+'?page=2')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(res.context['book_list']) == 5)


class BookDetailViewTest(TestCase):
    """Testing the book detail view"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_author = Author.objects.create(
            first_name="Test Author",
            last_name="Test Author last"
        )
        cls.test_book = Book.objects.create(
            title="Test Book",
            isbn="1234567890",
            author=cls.test_author,
            summary="Test Summary"
        )

    def test_book_detail_view_existing_book(self):
        """Testing existing book for a the detail book"""
        res = self.client.get(
            reverse('app_catalog:book-detail', kwargs={'pk': self.test_book.pk})  # noqa
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.test_book.title)
        self.assertContains(res, self.test_author.first_name)
        self.assertContains(res, self.test_book.summary)

    def test_book_detail_view_template(self):
        """Testing if the right template was used for detial book view"""
        res = self.client.get(
            reverse('app_catalog:book-detail', kwargs={'pk': self.test_book.pk})  # noqa
        )
        self.assertTemplateUsed(res, 'app_catalog/book_detail.html')

    def test_book_detail_view_none_existing_book(self):
        """Testing page not found for non existing view"""
        res = self.client.get(
            reverse('app_catalog:book-detail', kwargs={'pk': 999})
        )
        self.assertEqual(res.status_code, 404)


class AuthorListViewTest(TestCase):
    """Testing Author list view"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        num_test_authors = 10
        for i in range(num_test_authors):
            Author.objects.create(
                first_name=f"First name {i}",
                last_name=f"Last name {i}"
            )

    def test_list_author_view(self):
        """Testing if all author are retrived corectly"""
        res = self.client.get(reverse('app_catalog:authors'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'app_catalog/author_list.html')
        self.assertTrue(len(res.context['author_list']) > 0)

    def test_pagination_is_5_author_view(self):
        """Testing pagination for the all author view"""
        res = self.client.get(reverse('app_catalog:authors'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['author_list']), 5)

        res = self.client.get(reverse('app_catalog:authors')+'?page=2')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context['author_list']), 5)


class AuthorDetailViewTest(TestCase):
    """Testing the Author detail view"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_author = Author.objects.create(
            first_name="Test Author",
            last_name="Test Author last",
            date_of_birth=date(1990, 1, 1),
            date_of_death=date(2020, 12, 31)
        )
        cls.test_book = Book.objects.create(
            title="Test Book",
            isbn="1234567890",
            author=cls.test_author,
            summary="Test Summary"
        )

    def test_author_detail_view_existing_book(self):
        """Testing existing template for a the detail author view"""
        res = self.client.get(
            reverse('app_catalog:author-detail', kwargs={'pk':self.test_author.pk})  # noqa
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.test_author.first_name)
        self.assertContains(res, self.test_author.last_name)
        self.assertContains(res, self.test_author.date_of_birth.strftime('%b. %#d, %Y'))  # noqa
        self.assertContains(res, self.test_author.date_of_death.strftime('%b. %#d, %Y'))  # noqa

    def test_author_detail_view_template(self):
        """Testing if the right template was used for detial author view"""
        res = self.client.get(
            reverse('app_catalog:author-detail', kwargs={'pk':self.test_author.pk})  # noqa
        )
        self.assertTemplateUsed(res, 'app_catalog/author_detail.html')

    def test_author_detail_view_none_existing_book(self):
        """Testing page not found for non existing view"""
        res = self.client.get(
            reverse('app_catalog:author-detail', kwargs={'pk': 999})
        )
        self.assertEqual(res.status_code, 404)


class LoanedBookByUserListViewTest(TestCase):
    """Testing the LoanedBookByUserListView"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username='teadasda',
            password='teadasda',
        )
        cls.user_2 = get_user_model().objects.create_user(
            username='teadasda2',
            password='teadasda2',
        )
        # creating some test BookInstaces with 'o' status
        cls.test_author = Author.objects.create(
            first_name="Test Author",
            last_name="Test Author last"
        )
        cls.test_book = Book.objects.create(
            title="Test Book",
            isbn="1234567890",
            author=cls.test_author,
            summary="Test Summary"
        )
        cls.due_date = date.today() + timedelta(days=10)
        cls.book_instace_1 = BookInstance.objects.create(
            book=cls.test_book,
            status='o',
            imprint='Test Imprint 1',
            due_back=cls.due_date,
            borrower=cls.user,
        )
        cls.due_date = cls.due_date - timedelta(days=1)
        cls.book_instace_2 = BookInstance.objects.create(
            book=cls.test_book,
            status='o',
            imprint='Test Imprint 2',
            due_back=cls.due_date,
            borrower=cls.user,
        )
        cls.book_instace_3 = BookInstance.objects.create(
            book=cls.test_book,
            status='o',
            imprint='Test Imprint 2',
            due_back=cls.due_date,
            borrower=cls.user_2,
        )

    def test_redirect_if_not_logged_in(self):
        """testing that the link redirects if the user is not logged in"""
        res = self.client.get(reverse('app_catalog:borrowed-books'))
        self.assertTrue(res.status_code, 302)  # redirection
        self.assertRedirects(
            res,
            reverse('login') + '?next=' + reverse('app_catalog:borrowed-books')
        )

    def test_logged_in_users_correct_template(self):
        """Testing if the right tempalte was used for a logged in user"""
        self.client.force_login(self.user)
        res = self.client.get(reverse('app_catalog:borrowed-books'))
        self.assertTrue(res.status_code, 200)
        self.assertTemplateUsed(
            res,
            'app_catalog/bookinstance_list_borrowed_user.html'
        )

    def test_logged_in_user_can_see_borrowed_books(self):
        """testing if authenticated user can see borrowed books"""
        self.client.force_login(self.user)
        res = self.client.get(reverse('app_catalog:borrowed-books'))
        self.assertEqual(str(res.context['user']), self.user.username)
        self.assertTrue('bookinstance_list' in res.context)
        self.assertEqual(len(res.context['bookinstance_list']), 2)

    def test_logged_in_user_books_in_corect_order(self):
        """testing if listed books are in correct order"""
        self.client.force_login(self.user)
        res = self.client.get(reverse('app_catalog:borrowed-books'))
        self.assertTrue('bookinstance_list' in res.context)
        book_list = res.context['bookinstance_list']
        # chekcing the order
        self.assertEqual(book_list[1], self.book_instace_1)
        self.assertEqual(book_list[0], self.book_instace_2)


class AllBorrowedBooksByUserListViewTest(TestCase):
    """Testing the AllBorrowedBooksByUserListView"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.USER_MODEL = get_user_model()
        # createing user with the req permission
        cls.password = 'testpass1245!@$!@%!saA'
        cls.user = cls.USER_MODEL.objects.create_user(
            username='testuser',
            password=cls.password
        )
        content_type = ContentType.objects.get_for_model(
            BookInstance
        )
        permission = Permission.objects.get(
            codename='can_view_staff',
            content_type=content_type,
        )
        cls.user.user_permissions.add(permission)

        # creating some test BookInstaces with 'o' status
        cls.test_author = Author.objects.create(
            first_name="Test Author",
            last_name="Test Author last"
        )
        cls.test_book = Book.objects.create(
            title="Test Book",
            isbn="1234567890",
            author=cls.test_author,
            summary="Test Summary"
        )
        cls.due_date = date.today() + timedelta(days=1)
        cls.book_instace_1 = BookInstance.objects.create(
            book=cls.test_book,
            status='o',
            imprint='Test Imprint 1',
            due_back=cls.due_date,
        )
        cls.book_instace_2 = BookInstance.objects.create(
            book=cls.test_book,
            status='o',
            imprint='Test Imprint 2',
            due_back=cls.due_date,
        )
        cls.book_instace_3 = BookInstance.objects.create(
            book=cls.test_book,
            status='m',
            imprint='Test Imprint 2',
            due_back=cls.due_date,
        )

    def test_redirect_if_not_logged_in(self):
        """testing redicrection if currect user not logged in"""
        res = self.client.get(reverse('app_catalog:borrowed-all'))
        self.assertEqual(res.status_code, 302)  # redirection
        self.assertRedirects(
            res,
            reverse('login') + '?next=' + reverse('app_catalog:borrowed-all')
        )

    def test_view_url_accessible_by_logged_in_user_with_permission(self):
        """testing if a user with aropraite permision can acces the view"""
        self.client.login(
            username=self.user.username,
            password=self.password,
        )
        res = self.client.get(reverse('app_catalog:borrowed-all'))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_correct_template(self):
        """testing the view using the correct template"""
        self.client.login(
            username=self.user.username,
            password=self.password,
        )
        res = self.client.get(reverse('app_catalog:borrowed-all'))
        self.assertTemplateUsed(
            res,
            'app_catalog/bookinstance_list_borrowed.html'
        )

    def test_queryset_returns_borrowed_books(self):
        """testing if the view returns the query set as expected"""
        self.client.login(
            username=self.user.username,
            password=self.password,
        )
        res = self.client.get(reverse('app_catalog:borrowed-all'))
        self.assertTrue('bookinstance_list' in res.context)
        self.assertEqual(len(res.context['bookinstance_list']), 2)


class RenewBookLibrarianViewTest(TestCase):
    """testing the RenewBookLibrarianView"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        """start setup"""
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='retrea24tgq3',
        )
        cls.user.user_permissions.add(
            Permission.objects.get(codename='can_renew'),
            Permission.objects.get(codename='can_view_staff'),
            Permission.objects.get(codename='can_mark_returned'),
        )
        cls.test_author = Author.objects.create(
            first_name="Test Author",
            last_name="Test Author last"
        )
        cls.test_book = Book.objects.create(
            title="Test Book",
            isbn="1234567890",
            author=cls.test_author,
            summary="Test Summary"
        )
        cls.book_instace = BookInstance.objects.create(
            book=cls.test_book,
            due_back=date.today() + timedelta(days=7)
        )

    def test_renew_book_librarian_view_redirect_if_not_logged_in(self):
        """testing redirect if the view accessed by a anonymous user"""
        res = self.client.get(
            reverse('app_catalog:renew-book-librarian',
                    kwargs={'pk': self.book_instace.pk}),
        )
        self.assertEqual(res.status_code, 302)

    def test_renew_book_librarian_view_uses_correct_template(self):
        """testing if the correct template is being rendered"""
        self.client.login(
            username=self.user.username,
            password='retrea24tgq3'
        )
        res = self.client.get(
            reverse('app_catalog:renew-book-librarian',
                    kwargs={'pk': self.book_instace.pk}),
        )
        self.assertTemplateUsed(res, 'app_catalog/book_renew_librarian.html')

    def test_renew_book_librarian_view_permission_required(self):
        """Testing if the permissions are corectly enforced - lacking"""
        user = get_user_model().objects.create(
            username='otheruser',
            password='otheruser'
        )
        self.client.force_login(user)
        res = self.client.get(
            reverse('app_catalog:renew-book-librarian',
                    kwargs={'pk': self.book_instace.pk}),
        )
        # forbidden - lack of permission
        self.assertEqual(res.status_code, 403)

    def test_renew_book_librarian_view_with_valid_permission(self):
        """Testing if the permissions are corectly enforced - valid"""
        self.client.login(
            username=self.user.username,
            password='retrea24tgq3'
        )
        valid_date = date.today() + timedelta(weeks=3)
        res = self.client.post(
            reverse('app_catalog:renew-book-librarian',
                    kwargs={'pk': self.book_instace.pk}),
            {'due_back': valid_date}
        )
        # check if the renewal was succesful and redirected
        # to the borrowed books list
        self.assertEqual(res.status_code, 302)  # redirect
        self.assertRedirects(res, reverse('app_catalog:borrowed-all'))

        # check if the due_back date was updated
        updated_book_instace = BookInstance.objects.get(
            pk=self.book_instace.pk
        )
        self.assertEqual(updated_book_instace.due_back, valid_date)

    def test_renew_book_librarian_view_with_invalid_date(self):
        """Testing invalid date for the renew book"""
        self.client.login(
            username=self.user.username,
            password='retrea24tgq3'
        )
        invalid_date = date.today() - timedelta(weeks=3)
        res = self.client.post(
            reverse('app_catalog:renew-book-librarian',
                    kwargs={'pk': self.book_instace.pk}),
            {'due_back': invalid_date}
        )
        # check if the form is not valid
        # and the page is displayed iwth the errors
        self.assertEqual(res.status_code, 200)
        self.assertFormError(
            res, 'form', 'due_back',
            'Invalid date - renewal in the past')


class AuthorViewsTest(TestCase):
    """Testing views for creation, updating and deletion of an author"""
    # setUpTestData: Run once to set up non-modified
    # data for all class methods.
    # setUp: Run once for every test method to setup clean data
    @classmethod
    def setUpTestData(cls) -> None:
        cls.password_hash = make_password('testpassworddsa')
        cls.user = get_user_model().objects.create(
            username='testuser',
            password=cls.password_hash
        )
        cls.user.user_permissions.add(
            Permission.objects.get(codename='view_author'),
            Permission.objects.get(codename='add_author'),
            Permission.objects.get(codename='change_author'),
            Permission.objects.get(codename='delete_author'),
        )

    def test_author_create_view_with_perm(self):
        """testing the creation of an author"""
        self.client.login(
            username=self.user.username,
            password='testpassworddsa'
        )
        res = self.client.get(reverse('app_catalog:author-create'))
        self.assertEqual(res.status_code, 200)
        author_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1980-01-01',
            'date_of_death': '2020-11-06',
        }
        res = self.client.post(
            reverse('app_catalog:author-create'),
            data=author_data
        )
        self.assertEqual(res.status_code, 302)
        author_exists = Author.objects.filter(
            first_name='John',
            last_name='Doe'
        ).exists()
        self.assertTrue(author_exists)

    def test_author_create_view_without_perm(self):
        """testing the creation of an author with
        a user witout the permision"""
        user = get_user_model().objects.create(
            username='otheruser',
            password='otheruser'
        )
        self.client.force_login(user)
        res = self.client.get(reverse('app_catalog:author-create'))
        self.assertEqual(res.status_code, 403)  # forbidden

    def test_author_create_view_not_logged_user(self):
        """testing the creation of an author with a non uathenticated user"""
        res = self.client.get(reverse('app_catalog:author-create'))
        self.assertEqual(res.status_code, 302)  # redirection
        self.assertRedirects(
            res,
            reverse('login') + '?next=' + reverse('app_catalog:author-create')
        )

    def test_author_update_view_with_perm(self):
        """testing author update view with a authenticated user"""
        self.client.login(
            username=self.user.username,
            password='testpassworddsa'
        )
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        res = self.client.get(
            reverse('app_catalog:author-update', args=[author.id])
        )
        self.assertEqual(res.status_code, 200)
        updated_data = {
            'first_name': 'Bob',
            'last_name': 'Markson'
        }
        res = self.client.post(
            reverse('app_catalog:author-update', args=[author.id]),
            data=updated_data,
        )
        self.assertEqual(res.status_code, 302)  # redirect
        updated_author = Author.objects.get(id=author.id)
        self.assertEqual(updated_author.first_name, updated_data['first_name'])
        self.assertEqual(updated_author.last_name, updated_data['last_name'])

    def test_author_update_view_without_perm(self):
        """testing the updating of an author with a user
        witout the permision"""
        user = get_user_model().objects.create(
            username='otheruser',
            password='otheruser'
        )
        self.client.force_login(user)
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        res = self.client.get(
            reverse('app_catalog:author-update', args=[author.id]),
        )
        self.assertEqual(res.status_code, 403)  # forbidden

    def test_author_update_view_not_logged_user(self):
        """testing the updating of an author with a non uathenticated user"""
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        res = self.client.get(
            reverse('app_catalog:author-update', args=[author.id]),
        )
        self.assertEqual(res.status_code, 302)  # redirection
        self.assertRedirects(
            res,
            reverse('login') + '?next=' + reverse('app_catalog:author-update', args=[author.id]),  # noqa
        )

    def test_author_delete_view_with_perm(self):
        """testing author delete view with a authenticated user"""
        self.client.login(
            username=self.user.username,
            password='testpassworddsa'
        )
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        url = reverse('app_catalog:author-delete', args=[author.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        total_authors = Author.objects.all().count()
        self.assertEqual(total_authors, 1)
        # deleting an author
        res = self.client.post(url)
        self.assertEqual(res.status_code, 302)  # redirect
        total_authors = Author.objects.all().count()
        self.assertEqual(total_authors, 0)

    def test_author_delete_view_without_perm(self):
        """testing the deletion of an author with a user
        witout the permision"""
        user = get_user_model().objects.create(
            username='otheruser',
            password='otheruser'
        )
        self.client.force_login(user)
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        res = self.client.get(
            reverse('app_catalog:author-delete', args=[author.id]),
        )
        self.assertEqual(res.status_code, 403)  # forbidden

    def test_author_delete_view_not_logged_user(self):
        """testing the deletion of an author with a non uathenticated user"""
        author = Author.objects.create(
            first_name='John',
            last_name='Doe',
        )
        url = reverse('app_catalog:author-delete', args=[author.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 302)  # redirection
        self.assertRedirects(
            res,
            reverse('login') + '?next=' + url,
        )

# TODO: add more tests
# same test for book - create, delete and update
