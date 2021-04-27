# school administration API 

version 1.0

## Description:
This is going to be a back end api of students, teachers, and classes. There will a seperate repo for a react front end that will consume this API.

This is a portfolio project, but I want it to seem like this API is real. So I want to fill this API with data from a school that I have created myself. I have mapped out buidlings, rooms, created semesters and courses. There is a filler.py file that is strictly for filling the database with information so the front end has more data to work with.

to generate the campus, staff, and students:


`python manage.py shell`


`from school_api.filler import generate_fake_campus, generate_person_type, generate_fake_people`


`generate_fake_campus` will fill the database with a school, buildings, rooms, and give the school and each building an address.

`generate_person_type` will fill the database with roles for people. Students, Teachers, and Teaching Assistants.

`generate_fake_people(number_of_people, person_type_primary_key)` will fill the database with people of a desired type. 1 for students, 2 for teachers, 3 for TA's.



## Visuals
![Entity Relationship Diagram](readmemedia/newERD.jpeg)
I want to keep the data in this API tidy so I read up on relational database planning and came up with this ERD to help me plan out my models. It feels pretty clean compared to my original effort.



## endpoints:
set up soon....


## Project status
Actively in development.