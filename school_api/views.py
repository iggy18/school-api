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
    search_fields = ['^first_name', '^last_name', '=person_id', 'person_type_id__person_type',]



class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



class CampusList(generics.ListAPIView):
    serializer_class = BuildingSerializer

    def get_queryset(self):
        queryset = Building.objects.all()
        building = self.request.query_params.get('building')
        
        if building is not None:
            queryset = queryset.filter(name__istartswith=building)
        
        return queryset



class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        subject = self.request.query_params.get('subject')
        teacherfirst = self.request.query_params.get('teacherfirst')
        teacherlast = self.request.query_params.get('teacherlast')

        if subject is not None:
            queryset = queryset.filter(subject_id__name=subject)
        
        if teacherfirst is not None:
            queryset = queryset.filter(teacher_id__first_name__iexact=teacherfirst)
        
        if teacherlast is not None:
            queryset = queryset.filter(teacher_id__last_name__iexact=teacherlast)
        
        return queryset
        
    
