from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import (
    SignupForm,
    NicknameChangeForm,
    LoginForm,
    PasswordChangeForm,
)


User = get_user_model()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        account = get_object_or_404(User, pk=self.kwargs["pk"])
        return self.request.user == account


class SignupView(generic.CreateView):
    """ サインアップビュー """
    form_class = SignupForm
    success_url = reverse_lazy("accounts:signup_done")
    template_name = "accounts/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "breadcrumb": "Account - サインアップ",
        }
        context.update(signup_context)
        return context


class SignupDoneView(generic.TemplateView):
    """サインアップ済ビュー"""
    template_name = 'accounts/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        signup_context = {
            "title": "Sign Up",
            "breadcrumb": "Account - サインアップ",
            "h1": "サインアップが完了しました。",
            "p": "データベース管理者にログイン権限を与えてもらってください。",
        }
        context.update(signup_context)
        return context


class LoginView(LoginView):
    """ログインビュー"""
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_context = {
            "breadcrumb": "Account - ログイン",
        }
        context.update(login_context)
        return context
    
    def form_valid(self, form):
        messages.info(self.request, 'ログインに成功しました。')
        return super().form_valid(form)


class LogoutConfirmView(LoginRequiredMixin, generic.TemplateView):
    """ログアウト確認ビュー"""
    template_name = 'accounts/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logout_context = {
            "breadcrumb": "Account - ログアウト",
        }
        context.update(logout_context)
        return context


class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトビュー"""
    template_name = 'accounts/login.html'


class NicknameChangeView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    """ ニックネーム変更ビュー """
    model = User
    form_class = NicknameChangeForm
    success_url = reverse_lazy("accounts:nickname_change_done")
    template_name = "accounts/nickname_change.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nickname_context = {
            "breadcrumb": "Account - ニックネーム変更",
        }
        context.update(nickname_context)
        return context


class NicknameChangeDoneView(generic.TemplateView):
    """サインアップ済ビュー"""
    template_name = 'accounts/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nickname_context = {
            "title": "Nickname Change",
            "breadcrumb": "Account - ニックネーム変更",
            "h1": "ニックネームを変更しました。",
            "p": "変更したい場合は何度でもできます。",
        }
        context.update(nickname_context)
        return context


class PasswordChangeView(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy("accounts:password_change_done")
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        password_context = {
            "breadcrumb": "Account - パスワード変更",
        }
        context.update(password_context)
        return context


class PasswordChangeDoneView(PasswordChangeDoneView):
    """パスワード変更済ビュー"""
    template_name = 'accounts/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        password_context = {
            "title": "Password Change",
            "breadcrumb": "Account - パスワード変更",
            "h1": "パスワードを変更しました",
            "p": "パスワードを忘れた場合は、管理者にパスワードを変更してもらってください。",
        }
        context.update(password_context)
        return context
