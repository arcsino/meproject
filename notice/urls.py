from django.urls import path
from . import views


app_name = "notice"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("about_signup/", views.AboutSignupView.as_view(), name="about_signup"),
    path("terms_of_use/", views.TermsOfUseView.as_view(), name="terms_of_use"),
    path("privacy_policy/", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
]