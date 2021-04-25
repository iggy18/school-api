from .models import Student, Teacher, Address
from faker import Faker
import random

fake = Faker()
CITIES = ["Seattle", "Redmond", "Kent", "Lynnwood", "Shoreline", "Edmonds"]
ZIPCODES = [98105, 98133, 98134, 98102, 98201, 98555]

def generate_fake_students(num):
    for i in range(1, num+1):
        street_address = fake.street_address()
        index_num = random.randint(0,5)
        city = CITIES[index_num]
        state = "WA"
        zipcode = ZIPCODES[index_num]
        student_address = Address(street_address=street_address, city=city, state=state, zipcode=zipcode)
        student_address.save()

        first_name= fake.first_name()
        last_name= fake.last_name()
        email = fake.email()
        student = Student(first_name=first_name, last_name=last_name, email=email, address_id=student_address)
        student.save()

def generate_fake_teachers(num):
    for i in range(1, num+1):
        street_address = fake.street_address()
        index_num = random.randint(0,5)
        city = CITIES[index_num]
        state = "WA"
        zipcode = ZIPCODES[index_num]
        teacher_address = Address(street_address=street_address, city=city, state=state, zipcode=zipcode)
        teacher_address.save()

        first_name= fake.first_name()
        last_name= fake.last_name()
        email = fake.email()
        teacher = Teacher(first_name=first_name, last_name=last_name, email=email, address_id=teacher_address)
        teacher.save()
