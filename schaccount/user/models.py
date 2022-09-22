from django.db import models

# Create your models here.


class AddStaff(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=500, null=True)
    soo = models.Choices()
