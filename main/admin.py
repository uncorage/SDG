from django.contrib import admin
from .models import Goal, ReportActive, TaskActive

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('number', 'title')
    search_fields = ('title',)
    ordering = ('number',)

@admin.register(TaskActive)
class TaskActiveAdmin(admin.ModelAdmin):
    list_display = ('goal',)
    search_fields = ('goal', 'task')
    ordering = ('date_created',)

@admin.register(ReportActive)
class ReportActiveAdmin(admin.ModelAdmin):
    list_display = ('goal',)
    search_fields = ('goal', 'description')
    ordering = ('date_reported',)