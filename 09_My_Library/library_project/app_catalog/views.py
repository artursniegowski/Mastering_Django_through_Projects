from app_catalog.forms import RenewBookModelForm
from app_catalog.models import (
    Author,
    Book,
    BookInstance,
    Genre
)
# from datetime import timedelta
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
# from django.db import IntegrityError
from django.db.models.query import QuerySet
# from django.http import HttpRequest, HttpResponseRedirect
# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from typing import Any


class IndexView(TemplateView):
    """Basic view for the index page"""
    template_name = 'app_catalog/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Setting the context data for the view"""
        context = super().get_context_data(**kwargs)

        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()

        num_instaces_available = BookInstance.objects.filter(
            status__exact='a'
        ).count()

        num_authors = Author.objects.count()
        num_genres = Genre.objects.all().count()

        # number of visits to this views - counted in the session variable
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1

        context.update({
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instaces_available': num_instaces_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_visits': num_visits,
        })

        return context


class BasePaginationListView(ListView):
    """Default settings for pagination"""
    paginate_by = 5


class BookListView(BasePaginationListView):
    """List view for all the books"""
    model = Book
    # paginate_by = 5
    # # can be change to anythong
    # context_object_name = 'book_list'
    # # filtering the query set
    # queryset = Book.objects.filter(
    #     title_icontains='war'
    # )[:5]
    # template_name = 'app_catalog/book_list.html'

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Book.objects.filter(title_icontains='war')[:5]


class BookDetailView(DetailView):
    """Detail view of a book"""
    model = Book


class AutorListView(BasePaginationListView):
    """List view for all the authors"""
    model = Author


class AuthorDetailView(DetailView):
    """Detail view of a Author"""
    model = Author


class LoanedBookByUserListView(LoginRequiredMixin, BasePaginationListView):
    """Listing all books that are loaned to the current user"""
    # model = BookInstance
    template_name = 'app_catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        # Get all book instances taht are loaned to the current user
        return BookInstance.objects.filter(
            borrower=self.request.user,
            status='o'
        ).order_by('due_back')


class AllBorrowedBooksByUserListView(
        LoginRequiredMixin, PermissionRequiredMixin, BasePaginationListView):
    """Listing all borrowed books, visible only for users
    haveing the given permission"""
    template_name = 'app_catalog/bookinstance_list_borrowed.html'
    paginate_by = 10
    permission_required = ['app_catalog.can_view_staff',]

    def get_queryset(self) -> QuerySet[Any]:
        # Get all bookinstaces that are loaned to any user
        return BookInstance.objects.filter(
            status='o',
        ).order_by('due_back')


# class RenewBookLibrarianView(
#         LoginRequiredMixin, PermissionRequiredMixin, View):
#     """handling the renewing book view"""
#     template_name = 'app_catalog/book_renew_librarian.html'
#     permission_required = ['app_catalog.can_renew',]

#     def create_renewal_form(self, request: HttpRequest, book_instance: BookInstance):  # noqa
#         """creating the correct form with initial data"""
#         if request.method == 'POST':
#             return RenewBookForm(request.POST)
#         return RenewBookForm(initial={
#             # proposed renewal date, 3 weeks from the old one
#             'renewal_date': book_instance.due_back + timedelta(weeks=3)
#         })

#     def get_book_instance(self, pk):
#         """returning a bookinstace for the given pk or a 404"""
#         return get_object_or_404(BookInstance, pk=pk)

#     def get(self, request: HttpRequest, pk):
#         """handling the GET request"""
#         book_instance = self.get_book_instance(pk)
#         form = self.create_renewal_form(request, book_instance)

#         context = {'form': form, 'book_instance': book_instance}
#         return render(request, self.template_name, context)

#     def post(self, request: HttpRequest, pk):
#         """handling the POST request"""
#         book_instance = self.get_book_instance(pk)
#         form = self.create_renewal_form(request, book_instance)

#         if form.is_valid():
#             try:
#                 book_instance.due_back = form.cleaned_data['renewal_date']
#                 book_instance.save()
#                 return HttpResponseRedirect(
#                     reverse('app_catalog:borrowed-all')
#                 )
#             except IntegrityError:
#                 form.add_error(None, "An integrity Error occured while saving the record.")  # noqa

#         context = {'form': form, 'book_instance': book_instance}
#         return render(request, self.template_name, context)

class RenewBookLibrarianView(
        LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """handling the renewing book view"""
    model = BookInstance
    form_class = RenewBookModelForm
    context_object_name = 'book_instance'
    template_name = 'app_catalog/book_renew_librarian.html'
    permission_required = ['app_catalog.can_renew',]
    success_url = reverse_lazy('app_catalog:borrowed-all')

    # def get_success_url(self) -> str:
    #     return reverse('app_catalog:borrowed-all')


class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """view handling the creation of an author"""
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}
    permission_required = [
        'app_catalog.view_author',
        'app_catalog.add_author',
    ]


class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """view handling the update of the author"""
    model = Author
    fields = '__all__'
    permission_required = [
        'app_catalog.view_author',
        'app_catalog.change_author',
    ]


class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """view handling the deltion of an author"""
    model = Author
    success_url = reverse_lazy('app_catalog:authors')
    permission_required = [
        'app_catalog.view_author',
        'app_catalog.delete_author',
    ]


class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """view handling the creation of a Book"""
    model = Book
    fields = '__all__'
    permission_required = [
        'app_catalog.view_book',
        'app_catalog.add_book',
    ]


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """view handling the update of the Book"""
    model = Book
    fields = '__all__'
    permission_required = [
        'app_catalog.view_book',
        'app_catalog.change_book',
    ]


class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """view handling the deletion of a Book"""
    model = Book
    success_url = reverse_lazy('app_catalog:books')
    permission_required = [
        'app_catalog.view_book',
        'app_catalog.delete_book',
    ]
