from django.shortcuts import render

from django.http import HttpResponse

from django.db import connection

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
    class_list = StudentClass.objects.raw("SELECT * FROM edziennik_studentclass ORDER BY creation_year DESC, name")
    return render(request, 'classes.html', {'teacher': getTeacher(teacher_id), 'classes': class_list, 'all': True})

def myClasses(request, teacher_id):
    class_list = StudentClass.objects.raw("SELECT * FROM edziennik_studentclass WHERE tutor_id = " + teacher_id + " ORDER BY creation_year DESC, name")
    return render(request, 'classes.html', {'teacher': getTeacher(teacher_id), 'classes': class_list, 'num_classes': len(list(class_list)), 'all': False})

def students(request, teacher_id):
    
    success = None
    delete = request.POST.get('delete_id')
    if delete is not None:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM edziennik_student WHERE id = " + delete)
        success = True
    
    search = request.POST.get('search')
    search_sql = ""
    if search:
        search_sql = "AND (edziennik_student.name||' '||edziennik_student.surname) ILIKE '%%"+search+"%%'"
    
    student_list = Student.objects.raw("SELECT edziennik_student.* FROM edziennik_student, edziennik_studentclass WHERE edziennik_studentclass.id = edziennik_student.class_member_id "+search_sql+" ORDER BY edziennik_studentclass.creation_year DESC, edziennik_studentclass.name, edziennik_student.surname, edziennik_student.name")
    
    return render(request, 'students.html', {'teacher': getTeacher(teacher_id), 'students': student_list, 'all': True, 'search': search or '', 'success': success})

def myStudents(request, teacher_id):
    search = request.POST.get('search')
    search_sql = ""
    if search:
        search_sql = "AND (edziennik_student.name||' '||edziennik_student.surname) ILIKE '%%"+search+"%%'"
    
    student_list = Student.objects.raw("SELECT DISTINCT edziennik_student.*, edziennik_studentclass.* FROM edziennik_student, edziennik_studentclass, edziennik_lesson WHERE (edziennik_studentclass.id = edziennik_student.class_member_id "+search_sql+") AND (edziennik_studentclass.tutor_id = "+teacher_id+" OR (edziennik_lesson.teacher_id = "+teacher_id+" AND edziennik_lesson.student_class_id = edziennik_studentclass.id)) ORDER BY edziennik_studentclass.creation_year DESC, edziennik_studentclass.name, edziennik_student.surname, edziennik_student.name")
        
    return render(request, 'students.html', {'teacher': getTeacher(teacher_id), 'students': student_list, 'all': False, 'search': search or ''})

def oneClass(request, teacher_id, class_id):
    
    success = None
    if request.POST.get('tutor'):
        cursor = connection.cursor()
        cursor.execute("UPDATE edziennik_studentclass  SET tutor_id = " + request.POST['tutor'] + " WHERE id = " + class_id)
        success = True
    
    class_list = StudentClass.objects.raw("SELECT * FROM edziennik_studentclass WHERE id = " + class_id)
    student_list = Student.objects.raw("SELECT * FROM edziennik_student WHERE class_member_id = " + class_id + " ORDER BY surname, name")
    teacher_list = Teacher.objects.raw("SELECT * FROM edziennik_teacher")
    return render(request, 'class.html', {'teacher': getTeacher(teacher_id), 'class': class_list[0], 'students': student_list, 'teachers': teacher_list, 'success': success})

def oneStudent(request, teacher_id, student_id):

    success = None
    if request.POST.get('name') and request.POST.get('surname'):
        cursor = connection.cursor()
        cursor.execute("UPDATE edziennik_student  SET name = %s, surname = %s WHERE id = " + student_id, [request.POST['name'], request.POST['surname']])
        success = True
    if request.POST.get('class'):
        cursor = connection.cursor()
        cursor.execute("UPDATE edziennik_student  SET class_member_id = %s WHERE id = " + student_id, [request.POST['class']])
        success = True
    
    student_list = Student.objects.raw("SELECT * FROM edziennik_student WHERE id = " + student_id)
    class_list = Teacher.objects.raw("SELECT * FROM edziennik_studentclass ORDER BY creation_year DESC, name")
    return render(request, 'student.html', {'teacher': getTeacher(teacher_id), 'student': student_list[0], 'classes': class_list, 'new': False, 'success': success})

def createStudent(request, teacher_id):
    success = None
    error = None
    if request.POST.get('name') and request.POST.get('surname'):
        if request.POST.get('class'):
            cursor = connection.cursor()
            cursor.execute("INSERT INTO edziennik_student (name, surname, class_member_id) VALUES (%s, %s, %s)", [request.POST['name'], request.POST['surname'], request.POST['class']])
            success = True
        else:
            error = True
        
    class_list = Teacher.objects.raw("SELECT * FROM edziennik_studentclass ORDER BY creation_year DESC, name")
    return render(request, 'student.html', {'teacher': getTeacher(teacher_id), 'classes': class_list, 'new': True, 'success': success, 'error': error})
