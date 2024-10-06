from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Goal, TaskActive, ReportActive
from .globals import *
from .utils import parse_generated_sdg_quest_text


def generate_quest(goal_name, location):
    gen = get_sdg_quest_generator()
    task_description = gen.generate_sdg_quest(goal_name, location)
    return task_description


def generate_active_quest(request, goal_number):
    goal = get_object_or_404(Goal, number=goal_number)
    location = request.POST.get("location", "Ashgabat")
    goal_name = goal.title
    task_text = generate_quest(goal_name, location)
    task_args = parse_generated_sdg_quest_text(task_text)
    task = goal.tasks.create(**task_args)
    return render(request, 'main/active.html', {'task': task})


def index(request):
    goals = Goal.objects.all()
    return render(request, 'main/goal_list.html', {'goals': goals})


def goal_detail(request, goal_number):
    goal = get_object_or_404(Goal, number=goal_number)
    return render(request, 'main/goal_detail.html', {'goal': goal})


def report_list(request):
    reports = ReportActive.objects.all()  # Получаем все отчеты
    return render(request, 'report_list.html', {'reports': reports})


def task_list(request):
    tasks = TaskActive.objects.all()
    return render(request, 'main/task_list.html', {'tasks': tasks})
