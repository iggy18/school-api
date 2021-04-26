from django.contrib import admin
from .models import Address, School, Building, Room, PersonType, Person, Subject, Course, Semester, DayOfWeek, TimeSlot, StudentEnrollment

admin.site.register(Address)
admin.site.register(School)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(PersonType)
admin.site.register(Person)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(DayOfWeek)
admin.site.register(TimeSlot)
admin.site.register(StudentEnrollment)