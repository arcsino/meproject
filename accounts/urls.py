from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path(
        'password_change/',
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        'password_change/done/',
        views.CustomPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]