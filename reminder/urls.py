from django.urls import path
from . import views

app_name = 'reminder'

urlpatterns = [
    path('month/', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),

    path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),

    path('day/', views.DayCalendar.as_view(), name='day'),
    path('day/<int:year>/<int:month>/<int:day>/', views.DayCalendar.as_view(), name='day'),

    path('schedules/', views.ScheduleList.as_view(), name='schedule_list'),
    path('schedules/list/', views.ScheduleList.as_view(), name='schedule_list'),
    path('schedules/detail/<int:pk>/', views.ScheduleDetail.as_view(), name='schedule_detail'),
]