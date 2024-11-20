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


class AllList(LoginRequiredMixin, generic.TemplateView):
    """全リストを表示するビュー"""
    template_name = 'reminder/all.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hw = '課題'
        todo = 'To-Do'
        item = '持ち物'
        homework_context = {
            'breadcrumb': 'Reminder - 全リスト',
            'hw_schedules': Schedule.objects.filter(category__name__contains=hw).order_by('deadline'),
            'todo_schedules': Schedule.objects.filter(category__name__contains=todo).order_by('deadline'),
            'item_schedules': Schedule.objects.filter(category__name__contains=item).order_by('deadline'),
        }
        context.update(homework_context)
        return context


class HomeworkList(LoginRequiredMixin, generic.TemplateView):
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


class ToDoList(LoginRequiredMixin, generic.TemplateView):
    """To-Doリストを表示するビュー"""
    template_name = 'reminder/todo.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo = 'To-Do'
        todo_context = {
            'breadcrumb': 'Reminder - To-Doリスト',
            'todo_schedules': Schedule.objects.filter(category__name__contains=todo).order_by('deadline'),
        }
        context.update(todo_context)
        return context


class ItemList(LoginRequiredMixin, generic.TemplateView):
    """持ち物リストを表示するビュー"""
    template_name = 'reminder/item.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = '持ち物'
        item_context = {
            'breadcrumb': 'Reminder - 持ち物リスト',
            'item_schedules': Schedule.objects.filter(category__name__contains=item).order_by('deadline'),
        }
        context.update(item_context)
        return context
