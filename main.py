from datetime import date
import time
from random import randint
import timeit
import math

from names import get_first_name, get_last_name
from data.mongo_setup import global_init
from insert_data import (
    create_student,
    create_class,
    create_contact,
    create_grade,
    add_class_to_student,
    add_contact_to_student,
    add_grade_to_student,
)
from utils import get_random_birth, get_random_number, get_random_point

# For testing
# NUMBER_OF_CLASSES = 2
# NUMBER_OF_STUDENTS = 10

NUMBER_OF_CLASSES = 1000
NUMBER_OF_STUDENTS = 1000000


def main():
    global_init()

    # create 1.000.000 student records
    class_list = []
    # create 1000 classes
    print("Creating Class")
    start = timeit.default_timer()
    for i in range(NUMBER_OF_CLASSES):
        print(f"Epoch {i}/{NUMBER_OF_CLASSES}:")
        temp_class = create_class(
            class_name="K" + str(math.trunc(i / 10) + 60),
            is_specialized=(randint(0, 1) == 1),
            year_start=math.trunc(i / 10) + 2018,
            year_end_seed=randint(4, 5),
        )
        class_list.append(temp_class)
    stop = timeit.default_timer()
    print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))

    print("Creating student")
    for i in range(NUMBER_OF_STUDENTS):
        print(f"Epoch {i}/{NUMBER_OF_STUDENTS}:")

        temp_student = create_student(
            name=get_first_name() + " " + get_last_name(), birth=get_random_birth()
        )
        add_class_to_student(class_list, temp_student)

        rand_email = (
            (get_first_name() if randint(0, 1) == 1 else get_last_name())
            + str(randint(0, 9999)).zfill(4)
            + "@vnu.edu.vn"
        )
        print(rand_email)
        temp_contact = create_contact(phone=get_random_number(), email=rand_email)
        add_contact_to_student(temp_contact, temp_student)

        number_of_semesters = randint(1, 4)
        for j in range(number_of_semesters):
            temp_grade = create_grade(
                semester_number=str(j + 1),
                math=get_random_point(),
                lang=get_random_point(),
                sci=get_random_point(),
            )
            add_grade_to_student(temp_grade, temp_student)

    stop = timeit.default_timer()
    print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))


if __name__ == "__main__":
    main()
