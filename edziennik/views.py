from django.shortcuts import render

from django.http import HttpResponse

from .models import *

def index(request):
    teacher_list = Teacher.objects.raw("SELECT * FROM edziennik_teacher")
    context = {'teachers': teacher_list}
    return render(request, 'index.html', context)

