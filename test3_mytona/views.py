from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    """Вход пользователя"""
    template_name = 'test3_mytona/login.html'


class UserLogoutView(LogoutView):
    """Выход пользователя"""
    success_url = reverse_lazy('main_page')


class SignUpView(CreateView):
    """Регистрация"""
    form_class = SignUpForm
    template_name = 'test3_mytona/signup.html'
    success_url = reverse_lazy('main_page')
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class MainPage(TemplateView):
    """Главная страница"""
    template_name = "test3_mytona/main.html"
