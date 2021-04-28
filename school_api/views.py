from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Address, Building, Course, DayOfWeek, Person, PersonType, Room, School, Semester, StudentEnrollment, Subject, TimeSlot
from .serializers import AddressSerializer, SchoolSerializer, BuildingSerializer, RoomSerializer, PersonTypeSerializer, PersonSerializer, SubjectSerializer, CourseSerializer, SemesterSerializer, DayOfWeekSerializer, TimeSlotSerializer, StudentEnrollmentSerializer 


@api_view(['GET'])
def main_view(request):
    api_urls = {
        'Key':'Value'
    }
    return Response(api_urls)

@api_view(['GET'])
def people_list(request):
    people = PersonType.objects.all()
    serializer = PersonTypeSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def campus_list(request):
    campus = School.objects.all()
    serializer = SchoolSerializer(campus, many=True)
    return Response(serializer.data)
