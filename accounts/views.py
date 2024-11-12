from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm, LoginForm, CustomPasswordChangeForm


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignUpView(CreateView):
    """ サインアップビュー """
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class CustomLoginView(LoginView):
    """ログインビュー"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトビュー"""
    template_name = 'accounts/login.html'


class CustomPasswordChangeView(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = 'accounts/password_change_form.html'


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    """パスワード変更済ビュー"""
    template_name = 'accounts/password_change_done.html'