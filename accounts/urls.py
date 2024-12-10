from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path(
        "signup/done/",
         views.SignupDoneView.as_view(),
         name="signup_done",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("logout_confirm/", views.LogoutConfirmView.as_view(), name="logout_confirm"),
    path(
        "nickname_change/<uuid:pk>/",
        views.NicknameChangeView.as_view(),
        name="nickname_change",
    ),
    path(
        "nickname_change/done/",
        views.NicknameChangeDoneView.as_view(),
        name="nickname_change_done",
    ),
    path(
        "password_change/",
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]