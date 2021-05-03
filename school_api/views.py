from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (Address, Building, Course, DayOfWeek, Person, PersonType, Room, School, Semester, StudentEnrollment, Subject, TimeSlot)

from .serializers import (AddressSerializer, BuildingSerializer, CourseSerializer, DayOfWeekSerializer, PersonSerializer, PersonTypeSerializer, RoomSerializer, SchoolSerializer, SemesterSerializer, StudentEnrollmentSerializer, SubjectSerializer, TimeSlotSerializer)


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
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^first_name', '^last_name', 'person__person_type']


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonSearch(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']

class CampusList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

