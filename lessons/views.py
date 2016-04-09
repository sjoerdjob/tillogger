from django.shortcuts import render

from .models import Lesson


def index(request):
    # Get first 5 lessons.
    lessons = Lesson.objects.all()[:5]

    return render(request, 'lessons/index.html', {'lessons': lessons})
