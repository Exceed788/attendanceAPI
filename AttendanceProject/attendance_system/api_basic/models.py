from django.db import models


# Create your models here.
class Student(models.Model):
    schoolID = models.CharField(max_length=10)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.schoolID, self.lastName, self.firstName, self.course, self.year


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name, self.time