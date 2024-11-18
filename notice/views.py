from django.views.generic import TemplateView, ListView
from .models import Notice

class IndexView(ListView):
    """ ホームビュー """
    template_name = "notice/index.html"
    queryset = Notice.objects.order_by("-date_created")
    context_object_name = "notice"
    paginate_by = 5
