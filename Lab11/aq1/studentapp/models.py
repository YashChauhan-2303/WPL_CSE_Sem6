from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=30, unique=True)
    student_name = models.CharField(max_length=120)
    course_name = models.CharField(max_length=120)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.student_id} - {self.student_name}"
