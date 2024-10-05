from django.shortcuts import render, get_object_or_404
from .models import Goal


def index(request):
    goals = Goal.objects.all()
    return render(request, 'main/goal_list.html', {'goals': goals})

def goal_detail(request, goal_number):
    goal = get_object_or_404(Goal, number=goal_number)
    return render(request, 'main/goal_detail.html', {'goal': goal})