from .models import Address, School, Building, Room, PersonType, Person, Subject, Course, Semester, DayOfWeek
from faker import Faker
from .classes import classes
import random

fake = Faker()


def generate_fake_address():
    '''
    this function generates fake street adresses, randomly assigns a city and it's zip, and saves it to the database
    '''


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
    '''
    this funtion generates the roles for people in the school and saves them to the database
    '''
    ROLES = ['Student', 'Teacher', 'Teaching Assistant']
    for role in ROLES:
        person_type = PersonType(person_type=role)
        person_type.save()


def generate_fake_people(num, person_type_pk):
    '''
    this function generates a fake address, a fake person, and selects the type of person. It takes in the number of people you want to create, and the type of person you want them to be. they are saved to the database
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
    '''
    this function creates campus buildings and saves them to the database.
    '''
    school = School.objects.get(pk=1)
    BUILDINGS = ['Aurthur Building', 'Ford Building', 'Marvin Building', 'Slartibartfast Building', 'Trillian Building', 'Zaphod Building']
    for building_name in BUILDINGS:
        address = generate_fake_address();
        address.save()

        building = Building(name=building_name, address_id=address, school_id=school)
        building.save()


def fill_building_with_rooms(building_pk, number_of_rooms):
    '''
    this function takes in a building pk and fills the building with the specified number of rooms and saves them to the database.
    '''
    building_var = Building.objects.get(pk=building_pk)
    room_count = 101
    for room in range(1, number_of_rooms+1):
        room = Room(room_number=room_count, building_id=building_var)
        room.save()
        room_count += 1


def generate_subjects():
    '''
    this function generates academic subjects and saves them to the database
    '''
    SUBJECTS = ['math', 'science', 'history', 'language', 'geography', 'art', 'electives']
    for item in SUBJECTS:
        sub = Subject(name=item)
        sub.save()


def generate_days():
    '''
    this function generates the daily schedule for classes and saves it to the database
    '''
    DAYS = ['1, 3, 5', '2, 4']
    for item in DAYS:
        day = DayOfWeek(name=item)
        day.save()


def pick_classes(num):
    '''
    this function selects a specified number of classes from a larger list of scraped classes. it checks to make sure each class is unique and not None.
    '''
    results = []
    for i in range(1, num+1):
        pick = random.choice(classes)
        while pick in results or pick == None:
            pick = random.choice(classes)
        results.append(pick)
    return results


def generate_classes(num):
    ''' 
    this function selects classes from a list of real classes and assigns them a subject, teacher, and room number to be taught in. the class is saved to the database
    '''

    generate_subjects()

    subjects = Subject.objects.all()
    teachers = Person.objects.filter(person_type_id=2)
    rooms = Room.objects.all()
    picked_classes = pick_classes(num)
    teacher_number = 0
    teacher_class_number = 0
    room_counter = 0
    for course in picked_classes:
        subject_id = random.choice(subjects)
        name = course
        teacher_id = teachers[teacher_number]
        course = Course(subject_id=subject_id, name=name, teacher_id=teacher_id, room_id=rooms[room_counter])
        course.save()

        teacher_class_number += 1
        room_counter += 1

        if teacher_class_number == 4:
            teacher_number += 1
            teacher_class_number = 0
        if room_counter == 85:
            room_counter = 0


def generate_semesters():
    '''
    this function generates semesters and saves them to the database.
    '''
    SEMESTERS = ['fall', 'spring', 'summer']
    for semester in SEMESTERS:
        season = Semester(name='semester')
        season.save()


def generate_university():
    '''
    this function runs all the other functions in this file. it fills the database with fake information for a fake university.
    '''
    address = generate_fake_address()
    address.save()

    school = School(name='Alan Turing University', address_id=address)
    school.save()

    generate_person_type()
    
    generate_days()

    generate_semesters()

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

    #students
    generate_fake_people(4300, 1)

    #teachers
    generate_fake_people(215, 2)

    #TA's
    generate_fake_people(215, 3)

    #create classes, assign teacher, and room #
    generate_classes(860)