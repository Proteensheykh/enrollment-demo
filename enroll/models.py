from django.db import models
from datetime import datetime, date

# Create your models here.

class Person(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=11)
    
    
    def get_age(self):
        age = datetime.date(datetime.now()) - self.date_of_birth
        age = age.days // 365
        return age

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(Person):

    isInternational = models.BooleanField(default=False)



class Professor(Person):

    salary = models.FloatField()

class Course(models.Model):

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=7)
    min_students = models.IntegerField()
    max_students = models.IntegerField()
    start_date = models.DateTimeField()
    start_date = models.DateTimeField()
    professors = models.ManyToManyField(Professor)   
    
    def __str__(self):
        return self.code + " " + self.name

class Address(models.Model):

    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street_address = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=7)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_address + ", " + self.city + ', ' + self.state + ', ' + self.country


class Enroll(models.Model):

    date_enrolled = models.DateTimeField(auto_now_add=True)
    grade = models.FloatField(default=0.0)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

