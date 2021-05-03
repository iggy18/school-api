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
        fields = 'person_id', 'person_type_id', 'first_name', 'last_name', 'email', 'address_id'


class PersonTypeSerializer(serializers.ModelSerializer):
    people = PersonSerializer(source='person_set', many=True, read_only=True)

    class Meta:
        model = PersonType
        fields = 'person_type_id', 'person_type', 'people'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subject_id = serializers.StringRelatedField(many=False)
    teacher_id = serializers.StringRelatedField(many=False)
    room_id = serializers.StringRelatedField(many=False)
    class Meta:
        model = Course
        fields = 'course_id', 'name', 'subject_id', 'teacher_id', 'room_id'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class DayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfWeek
        fields = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = '__all__'

