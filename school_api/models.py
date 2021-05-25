from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.state} {self.zipcode}'


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=255)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.building_id}, {self.room_number}'


class PersonType(models.Model):
    person_type_id = models.AutoField(primary_key=True)
    person_type = models.CharField(max_length=255)

    def __str__(self):
        return self.person_type


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    person_type_id = models.ForeignKey(PersonType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.person_type_id}'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    teacher_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DayOfWeek(models.Model):
    day_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
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
    start_time = models.CharField(max_length=255, choices=TIME_CHOICES)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    day_id = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.start_time}, {self.course_id}'


class StudentEnrollment(models.Model):
    student_enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id}, {self.course_id}'