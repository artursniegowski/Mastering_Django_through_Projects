from typing import Any, Dict, Optional, Type
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from django.views.generic.base import View 
from app_add_models.models import UserModel, DjangoUserModel
from django.urls import reverse_lazy
import datetime
from sqlalchemy_test.settings import SA_DB_SESSION
from app_add_models.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
 

# Create your views here.
class UserListView(ListView):
    model = UserModel
    template_name = 'app_add_models/index.html'
    context_object_name = 'all_users'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_year']= datetime.datetime.now().year
        return context
    
    def get_queryset(self):        
        return UserModel.get_all()
    
class AddCreateView(FormView):
    model = DjangoUserModel
    template_name = 'app_add_models/add.html'
    form_class = UserForm
    # fields = ['first_name', 'last_name', 'email', 'description']
    success_url = reverse_lazy('app_add_models:home')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_year']= datetime.datetime.now().year
        return context
    
    # saving new user to the database if data is valid
    def form_valid(self, form) -> HttpResponse:
        new_user = UserModel(
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            description = form.cleaned_data['description'],
        )
        # new_user = form.save(commit=False)
        with SA_DB_SESSION() as db_session:
            db_session.add(new_user)
            db_session.commit()
        
        return HttpResponseRedirect(self.get_success_url())
        # preventing from saving the django model
        # return super().form_valid(form)
    
class DeleteUserView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk',None)
        
        if not pk:
            return HttpResponseBadRequest()
        
        with SA_DB_SESSION() as db_session:
            # querry the user with the given id
            user = db_session.get(UserModel, pk)
            
            if not user:
                return HttpResponseBadRequest()
            
            # TODO: error handling exception handling is missing - to add
            # if somehing happens witht he databse expetion need to be handled !
            db_session.delete(user)
            db_session.commit()
        
        # return HttpResponse(status=204)
        return HttpResponseRedirect(reverse('app_add_models:home'))