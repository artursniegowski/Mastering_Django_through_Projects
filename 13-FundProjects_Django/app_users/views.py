from app_users.forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginUserView(LoginView):
    template_name = 'app_users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('app_funding:home')

class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('app_funding:home')
