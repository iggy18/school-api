from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=90)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.state} {self.zipcode}'


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=150) 
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    School_id = models.ForeignKey(School, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Slot(models.Model):
    TIME_CHOICES = (
        ('07:00:00', '7 am'),
        ('08:00:00', '8 am'),
        ('09:00:00', '9 am'),
        ('11:00:00', '10 am'),
        ('12:00:00', '11 am'),
        ('13:00:00', '12 am'),
        ('14:00:00', '1 pm'),
        ('15:00:00', '2 pm'),
        ('16:00:00', '3 pm'),
    )
    slot_id = models.AutoField(primary_key=True)
    start_time = models.CharField(max_length=8, choices=TIME_CHOICES)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start_time}, {self.course_id}'


class StudentEnrollment(models.Model):
    student_enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id}, {self.course_id}'