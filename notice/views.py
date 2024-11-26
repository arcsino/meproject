from django.views.generic import TemplateView, ListView
from .models import Notice

class IndexView(ListView):
    """ ホームビュー """
    template_name = "notice/index.html"
    queryset = Notice.objects.order_by("-date_created")
    context_object_name = "notice"
    paginate_by = 5


class AboutSignupView(TemplateView):
    """サインアップ詳細ビュー"""
    template_name = "notice/about_signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_context = {
            "breadcrumb": "About - サインアップについて",
        }
        context.update(about_context)
        return context


class TermsOfUseView(TemplateView):
    """利用規約ビュー"""
    template_name = "notice/terms_of_use.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        terms_context = {
            "breadcrumb": "About - 利用規約",
        }
        context.update(terms_context)
        return context


class PrivacyPolicyView(TemplateView):
    """プライバシーポリシービュー"""
    template_name = "notice/privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        privacy_context = {
            "breadcrumb": "About - プライバシーポリシー",
        }
        context.update(privacy_context)
        return context
