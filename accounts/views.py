from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignupForm, LoginForm, PasswordChangeForm


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "accounts/index.html"


class SignupView(CreateView):
    """ サインアップビュー """
    form_class = SignupForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"


class LoginView(LoginView):
    """ログインビュー"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class LogoutConfirmView(LoginRequiredMixin, TemplateView):
    """ログアウト確認ビュー"""
    template_name = 'accounts/logout.html'


class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトビュー"""
    template_name = 'accounts/login.html'


class PasswordChangeView(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = 'accounts/password_change_form.html'


class PasswordChangeDoneView(PasswordChangeDoneView):
    """パスワード変更済ビュー"""
    template_name = 'accounts/password_change_done.html'