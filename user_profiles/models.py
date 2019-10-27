from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    # student registration info
    # Student.objects.get(id=2).registration_set.all()
    student_name = models.CharField(max_length=50)
    data_added = models.DateTimeField(auto_now_add=True)

    # other info
    college = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Course(models.Model):
    # course registration info:
    # Course.objects.get(id=1).registration_set.all()
    course_title = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, through='Registration')

    def __str__(self):
        return self.course_title


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return str(self.student) + ' ' + str(self.course) + ' ' + str(self.time)
