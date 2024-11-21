from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignupForm, LoginForm, PasswordChangeForm


class SignupView(CreateView):
    """ サインアップビュー """
    form_class = SignupForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - サインアップ",
        }
        context.update(signup_context)
        return context


class LoginView(LoginView):
    """ログインビュー"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - ログイン",
        }
        context.update(signup_context)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'ログインに成功しました。')
        return super().form_valid(form)


class LogoutConfirmView(LoginRequiredMixin, TemplateView):
    """ログアウト確認ビュー"""
    template_name = 'accounts/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - ログアウト",
        }
        context.update(signup_context)
        return context


class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトビュー"""
    template_name = 'accounts/login.html'


class PasswordChangeView(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = 'accounts/password_change_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - パスワード変更",
        }
        context.update(signup_context)
        return context


class PasswordChangeDoneView(PasswordChangeDoneView):
    """パスワード変更済ビュー"""
    template_name = 'accounts/password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - パスワード変更",
        }
        context.update(signup_context)
        return context