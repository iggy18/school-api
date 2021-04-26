from .models import Person, PersonType, Address
from faker import Faker
import random

fake = Faker()
CITIES = ["Seattle", "Redmond", "Kent", "Lynnwood", "Shoreline", "Edmonds"]
ZIPCODES = [98105, 98133, 98134, 98102, 98201, 98555]

def generate_fake_people(num, person_type_pk):
    student = PersonType.objects.get(pk=1)
    teacher = PersonType.objects.get(pk=2)
    if person_type_pk == 1:
        person_type = student
    if person_type_pk == 2:
        person_type = teacher

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
        student = Person(first_name=first_name, last_name=last_name, email=email, person_type_id=person_type, address_id=student_address)
        student.save()
