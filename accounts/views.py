from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm


class IndexView(TemplateView):
    template_name = "index.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    # ～未完成～
