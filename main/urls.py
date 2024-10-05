from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goal/<int:goal_number>/', views.goal_detail, name='goal_detail'),
]