from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.employee_id} - {self.name}"
