from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import Category, Schedule
from .forms import ScheduleCreateForm
from . import mixins
import datetime


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
    """スケジュール一覧ビュー"""
    template_name = 'reminder/schedule_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        homework_context = {
            'breadcrumb': 'Reminder - スケジュール一覧',
            'schedules': Schedule.objects.filter(deadline__date__gte=today).order_by('deadline', 'subject'),
            'categories': Category.objects.order_by('pk'),
            'first_category': Category.objects.first(),
        }
        context.update(homework_context)
        return context


class ScheduleDetailView(LoginRequiredMixin, generic.DetailView):
    """スケジュール詳細を表示するビュー"""
    template_name = 'reminder/schedule_detail.html'
    model = Schedule
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homework_context = {
            'breadcrumb': 'スケジュール詳細',
            'categories': Category.objects.all(),
        }
        context.update(homework_context)
        return context


class ScheduleCreateView(LoginRequiredMixin, generic.CreateView):
    """スケジュール作成ビュー"""
    model = Schedule
    template_name = 'reminder/schedule_create.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('reminder:schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        create_context = {
            "breadcrumb": "Reminder - スケジュール作成",
        }
        context.update(create_context)
        return context
    
    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.created_by = str(self.request.user)
        schedule.updated_by = str(self.request.user)
        schedule.save()
        messages.success(self.request, 'スケジュールを作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'スケジュールの作成に失敗しました。')
        return super().form_invalid(form)


class ScheduleUpdateView(LoginRequiredMixin, generic.UpdateView):
    """スケジュール編集ビュー"""
    model = Schedule
    template_name = 'reminder/schedule_update.html'
    form_class = ScheduleCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context = {
            "breadcrumb": "スケジュール編集",
        }
        context.update(update_context)
        return context

    def get_success_url(self):
        return reverse_lazy('reminder:schedule_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        schedule = form.save(commit=False)
        schedule.updated_by = str(self.request.user)
        schedule.save()
        messages.info(self.request, 'スケジュールを更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'スケジュールの更新に失敗しました。')
        return super().form_invalid(form)


class ScheduleDeleteView(LoginRequiredMixin, generic.DeleteView):
    """スケジュール削除ビュー"""
    model = Schedule
    template_name = 'reminder/schedule_delete.html'
    success_url = reverse_lazy('reminder:schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update_context = {
            "breadcrumb": "スケジュール削除",
        }
        context.update(update_context)
        return context
    
    def form_valid(self, form):
        messages.error(self.request, 'スケジュールを削除しました。')
        return super().form_valid(form)