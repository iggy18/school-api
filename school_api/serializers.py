from rest_framework import serializers

from .models import Address, School, Building, Room, PersonType, Person, Subject, Course, Semester, DayOfWeek, TimeSlot, StudentEnrollment

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = 'room_id', 'room_number'

class BuildingSerializer(serializers.ModelSerializer):

    address_id = serializers.StringRelatedField(many=False)
    rooms = RoomSerializer(source='room_set', many=True, read_only=True)

    class Meta:
        model = Building
        fields = 'building_id', 'name', 'address_id', 'rooms'


class SchoolSerializer(serializers.ModelSerializer):
    address_id = serializers.StringRelatedField(many=False)
    buildings = BuildingSerializer(source='building_set', many=True, read_only=True)

    class Meta:
        model = School
        fields = 'school_id', 'name', 'address_id', 'buildings'


class PersonSerializer(serializers.ModelSerializer):
    address_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = Person
        fields = 'person_id', 'first_name', 'last_name', 'email', 'address_id'


class PersonTypeSerializer(serializers.ModelSerializer):
    people = PersonSerializer(source='person_set', many=True, read_only=True)

    class Meta:
        model = PersonType
        fields = 'person_type_id', 'person_type', 'people'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fiels = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fiels = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fiels = '__all__'


class DayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fiels = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fiels = '__all__'


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fiels = '__all__'

