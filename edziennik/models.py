from django.db import models

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return 'Subject: ' + self.name

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    
    def __str__(self):
        return 'Teacher: ' + self.surname + ' ' + self.name

class StudentClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    creation_year = models.DateField()
    tutor = models.ForeignKey(Teacher, related_name="pupil")
    teachers = models.ManyToManyField(Teacher)
    
    def __str__(self):
        return 'Class ' + self.name + ' ('+str(self.creation_year)+')'

    class Meta:
        verbose_name = "class"
        verbose_name_plural = "classes"

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    class_member = models.ForeignKey(StudentClass)
    
    def __str__(self):
        return 'Student: ' + self.surname + ' ' + self.name + ' (' + self.class_member.name + ')'

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    student_class = models.ForeignKey(StudentClass)
    date = models.DateTimeField()
    
    def __str__(self):
        return 'Lesson ' + self.subject.name + ' in ' + self.student_class.name + ' at ' + str(self.date)

class Grade(models.Model):
    GRADES = (
      (2, 2),
      (2.5, 2.5),
      (3, 3),
      (3.5, 3.5),
      (4, 4),
      (4.5, 4.5),
      (5, 5)
    )
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    weight = models.FloatField()
    value = models.DecimalField(decimal_places=1, max_digits=1, choices=GRADES)
    comment = models.TextField()
    
    def __str__(self):
        return 'Grade ' + value + ' for ' + str(self.student) + ' on ' + str(self.lesson)

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student)
    lesson = models.ForeignKey(Lesson)
    value = models.BooleanField(default=False)
    justified = models.NullBooleanField(default=None)
