from tkinter import CASCADE
from django.db import models

# Create your models here.


class AddStaff(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=500, null=True)
    soo = models.Choices()
    sex = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.first_name


class AddStudents(models.Model):
    student_id = models.ForeignKey(AddStaff, on_delete=CASCADE)
    Student_sch = models.CharField(max_length=120)
    student_parent = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.student_id
