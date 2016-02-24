from django.shortcuts import render

from django.http import HttpResponse

from .models import *

def getTeacher(teacher_id):
    teacher = Teacher.objects.raw("SELECT * FROM edziennik_teacher WHERE id="+teacher_id)
    return teacher[0]

def index(request):
    teacher_list = Teacher.objects.raw("SELECT * FROM edziennik_teacher")
    context = {'teachers': teacher_list}
    return render(request, 'index.html', context)

def teacher(request, teacher_id):
    return render(request, 'teacher.html', {'teacher': getTeacher(teacher_id)})

def lessons(request, teacher_id):
    lesson_list = Lesson.objects.raw("SELECT * FROM edziennik_lesson WHERE teacher_id = " + teacher_id + " ORDER BY date DESC")
    return render(request, 'lessons.html', {'teacher': getTeacher(teacher_id), 'lessons': lesson_list})

def classes(request, teacher_id):
    class_list = StudentClass.objects.raw("SELECT * FROM edziennik_studentclass ORDER BY creation_year DESC")
    return render(request, 'classes.html', {'teacher': getTeacher(teacher_id), 'classes': class_list, 'all': True})

def myClasses(request, teacher_id):
    class_list = StudentClass.objects.raw("SELECT * FROM edziennik_studentclass WHERE tutor_id = " + teacher_id + " ORDER BY creation_year DESC")
    return render(request, 'classes.html', {'teacher': getTeacher(teacher_id), 'classes': class_list, 'num_classes': len(list(class_list)), 'all': False})

def students(request, teacher_id):
    search = request.POST.get('search')
    if not search:
        student_list = Student.objects.raw("SELECT * FROM edziennik_student")
    else:
        student_list = Student.objects.raw("SELECT * FROM edziennik_student WHERE (name||' '||surname) ILIKE '%%"+search+"%%'")
    print(student_list)
    return render(request, 'students.html', {'teacher': getTeacher(teacher_id), 'students': student_list, 'all': True, 'search': search or ''})

def myStudents(request, teacher_id):
    search = request.POST.get('search')
    if not search:
        student_list = Student.objects.raw("SELECT * FROM edziennik_student")
    else:
        student_list = Student.objects.raw("SELECT * FROM edziennik_student WHERE (name||' '||surname) ILIKE '%%"+search+"%%'")
    print(student_list)
    return render(request, 'students.html', {'teacher': getTeacher(teacher_id), 'students': student_list, 'all': False, 'search': search or ''})
