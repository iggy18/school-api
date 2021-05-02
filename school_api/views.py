from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Address, Building, Course, DayOfWeek, Person, PersonType, Room, School, Semester, StudentEnrollment, Subject, TimeSlot
from .serializers import AddressSerializer, SchoolSerializer, BuildingSerializer, RoomSerializer, PersonTypeSerializer, PersonSerializer, SubjectSerializer, CourseSerializer, SemesterSerializer, DayOfWeekSerializer, TimeSlotSerializer, StudentEnrollmentSerializer 


@api_view(['GET'])
def main_view(request):
    api_urls = {
        'api paths': {
            'api/v1/people':'list of people and their roles',
            'api/v1/campus':'list of campus, buidlings, and rooms',
            'api/v1/class':'list of classes the university offers'
        }
    }
    return Response(api_urls)


class PeopleList(generics.ListAPIView):
    queryset = PersonType.objects.all()
    serializer_class = PersonTypeSerializer



class CampusList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer