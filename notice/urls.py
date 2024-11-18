from django.urls import path
from . import views


app_name = "notice"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("index/", views.IndexView.as_view(), name="index"),
]