from django.urls import path
from . import views

app_name = 'reminder'

urlpatterns = [
    path('month/', views.MonthCalendarView.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendarView.as_view(), name='month'),

    path('week/', views.WeekCalendarView.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendarView.as_view(), name='week'),

    path('day/', views.DayCalendarView.as_view(), name='day'),
    path('day/<int:year>/<int:month>/<int:day>/', views.DayCalendarView.as_view(), name='day'),

    path('schedules/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/list/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/detail/<int:pk>/', views.ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/create/', views.ScheduleCreateView.as_view(), name='schedule_create'),
]