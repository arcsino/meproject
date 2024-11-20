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

    path('schedules/', views.AllList.as_view(), name='all'),
    path('schedules/all/', views.AllList.as_view(), name='all'),
    path('schedules/homework/', views.HomeworkList.as_view(), name='homework'),
    path('schedules/todo/', views.ToDoList.as_view(), name='todo'),
    path('schedules/item/', views.ItemList.as_view(), name='item'),
]