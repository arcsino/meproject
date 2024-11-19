from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Schedule
from . import mixins


class MonthCalendar(LoginRequiredMixin, mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'reminder/month.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class WeekCalendar(LoginRequiredMixin, mixins.WeekCalendarMixin, generic.TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'reminder/week.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class DayCalendar(LoginRequiredMixin, mixins.DayCalendarMixin, generic.TemplateView):
    """日間カレンダーを表示するビュー"""
    template_name = 'reminder/day.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_day_calendar()
        context.update(calendar_context)
        return context


class HomeworkListView(LoginRequiredMixin, generic.TemplateView):
    """課題リストを表示するビュー"""
    template_name = 'reminder/homework.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hw = '課題'
        homework_context = {
            'breadcrumb': 'Reminder - 課題リスト',
            'hw_schedules': Schedule.objects.filter(category__name__contains=hw).order_by('deadline'),
        }
        context.update(homework_context)
        return context