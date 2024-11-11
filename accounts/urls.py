from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]