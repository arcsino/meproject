from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Schedule
from .forms import ScheduleCreateForm
from . import mixins


class MonthCalendarView(LoginRequiredMixin, mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'reminder/month.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class WeekCalendarView(LoginRequiredMixin, mixins.WeekCalendarMixin, generic.TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'reminder/week.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class DayCalendarView(LoginRequiredMixin, mixins.DayCalendarMixin, generic.TemplateView):
    """日間カレンダーを表示するビュー"""
    template_name = 'reminder/day.html'
    model = Schedule

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_day_calendar()
        context.update(calendar_context)
        return context


class ScheduleListView(LoginRequiredMixin, generic.TemplateView):
    """スケジュール一覧を表示するビュー"""
    template_name = 'reminder/schedule_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homework_context = {
            'breadcrumb': 'Reminder - スケジュール一覧',
            'schedules': Schedule.objects.order_by('deadline'),
            'categories': Category.objects.order_by('pk'),
            'first_category': Category.objects.first(),
        }
        context.update(homework_context)
        return context


class ScheduleDetailView(LoginRequiredMixin, generic.DetailView):
    """スケジュールの詳細を表示するビュー"""
    template_name = 'reminder/schedule_detail.html'
    model = Schedule
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homework_context = {
            'breadcrumb': 'スケジュールの詳細',
            'categories': Category.objects.all(),
        }
        context.update(homework_context)
        return context


class ScheduleCreateView(LoginRequiredMixin, generic.CreateView):
    """スケジュールの新規作成ビュー"""
    model = Schedule
    template_name = 'reminder/schedule_create.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('reminder:schedule_list')

    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.created_by = self.request.user
        schedule.updated_by = self.request.user
        schedule.save()
        messages.success(self.request, 'スケジュールを作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'スケジュールの作成に失敗しました。')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        create_context = {
            "breadcrumb": "Reminder - 新規作成",
        }
        context.update(create_context)
        return context
