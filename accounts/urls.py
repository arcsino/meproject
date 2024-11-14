from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('logout_confirm', views.LogoutConfirmView.as_view(), name="logout_confirm"),
    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]