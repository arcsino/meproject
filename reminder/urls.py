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
    path('homework/', views.HomeworkListView.as_view(), name='homework')
]