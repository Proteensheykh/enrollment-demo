from django.contrib import admin

from .models import Student, Professor, Course, Address, Enroll

# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Address)
admin.site.register(Enroll)
