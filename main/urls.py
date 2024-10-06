from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('goal/<int:goal_number>/', views.goal_detail, name='goal_detail'),
    path('active/<int:goal_number>/', views.generate_active_quest, name='active_view'),
    path('passive/<int:goal_number>/', views.goal_detail, name='passive_view'),
    path('reports/', views.report_list, name='report_list'),
    path('task_list/', views.task_list, name='task_list'),
]