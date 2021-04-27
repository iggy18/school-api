from .models import Address, School, Building, Room, PersonType, Person, Subject, Course, Semester, DayOfWeek
from faker import Faker
import random

fake = Faker()

def generate_fake_address():
    CITIES = ["Seattle", "Redmond", "Kent", "Lynnwood", "Shoreline", "Edmonds"]
    ZIPCODES = [98105, 98133, 98134, 98102, 98201, 98555]

    street_address = fake.street_address()
    index_num = random.randint(0,5)
    city = CITIES[index_num]
    state = "WA"
    zipcode = ZIPCODES[index_num]
    address = Address(street_address=street_address, city=city, state=state, zipcode=zipcode)
    return address

def generate_person_type():
    roles = ['Student', 'Teacher', 'Teaching Assistant']
    for role in roles:
        person_type = PersonType(person_type=role)
        person_type.save()

def generate_fake_people(num, person_type_pk):
    '''
    this function generates a fake address, a fake person, and selects the type of person to create. It takes in the number of people you want to create, and the type of person you want them to be.
    '''
    student = PersonType.objects.get(pk=1)
    teacher = PersonType.objects.get(pk=2)
    teaching_assistant = PersonType.objects.get(pk=3)

    if person_type_pk == 1:
        person_type = student
    if person_type_pk == 2:
        person_type = teacher
    if person_type_pk == 3:
        person_type = teaching_assistant

    for i in range(1, num+1):
        person_address = generate_fake_address()
        person_address.save()

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        student = Person(first_name=first_name, last_name=last_name, email=email, person_type_id=person_type, address_id=person_address)
        student.save()


def make_buildings():
    school = School.objects.get(pk=1)
    buildings = ['Aurthur Building', 'Ford Building', 'Marvin Building', 'Slartibartfast Building', 'Trillian Building', 'Zaphod Building']
    for building_name in buildings:
        address = generate_fake_address();
        address.save()

        building = Building(name=building_name, address_id=address, school_id=school)
        building.save()


def fill_building_with_rooms(building_pk, number_of_rooms):
    building_var = Building.objects.get(pk=building_pk)
    room_count = 101
    for room in range(1, number_of_rooms+1):
        room = Room(room_number=room_count, building_id=building_var)
        room.save()
        room_count += 1


def generate_campus():
    address = generate_fake_address()
    address.save()

    school = School(name='Alan Turing University', address_id=address)
    school.save()

    make_buildings()

    # aurthur
    fill_building_with_rooms(1, 19)

    # Ford
    fill_building_with_rooms(2, 12)

    # Marvin
    fill_building_with_rooms(3, 15)

    # Slartibartfast
    fill_building_with_rooms(4, 8)

    #Trillian
    fill_building_with_rooms(5, 17)

    #Zaphod
    fill_building_with_rooms(6, 15)


