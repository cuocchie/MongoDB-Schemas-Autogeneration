from names import get_first_name, get_full_name, get_last_name
from data.students import Student
from data.grades import Grade
from data.contact import Contact
from data.classes import Class
from utils import *

from datetime import date, timedelta
from random import randint, random


def create_student(name, birth) -> Student:

    student = Student()

    student.name = name
    student.birth = birth

    student.save()

    return student


def create_contact(phone, email) -> Contact:

    contact = Contact()

    contact.phone = phone
    contact.email = email

    return contact


def create_grade(semester_number: str, math, lang, sci) -> Grade:

    grade = Grade()

    grade.semester_number = semester_number
    grade.math = math
    grade.lang = lang
    grade.sci = sci
    print(math, lang, sci, sep="  ")
    grade.save()

    return grade


def create_class(
    class_name: str, is_specialized: bool, year_start: int, year_end_seed: int
) -> Class:
    new_class = Class()

    new_class.class_name = class_name
    new_class.is_specialized = randint(0, 1) == 1
    new_class.year_start = year_start
    new_class.year_end = year_start + year_end_seed

    new_class.save()

    return new_class


def add_contact_to_student(contact: Contact, student: Student):
    student.contact = contact
    student.save()


def add_grade_to_student(grade: Grade, student: Student):
    student.grade.append(grade.id)
    student.save()


def add_class_to_student(class_list: List, student: Student):
    student.class_id = class_list[get_random_class(class_list)].id
    student.save()
