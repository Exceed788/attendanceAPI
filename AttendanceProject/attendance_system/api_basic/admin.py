from django.contrib import admin
from .models import Event, Student
# Register your models here.


admin.site.register(Student)
admin.site.register(Event)