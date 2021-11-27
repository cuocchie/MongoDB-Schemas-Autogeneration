import logging
from random import randint
import random
import string
import time
import timeit
import mysql.connector
from get_random_name import get_name, get_name_list
from schemas import Classes, Students, Grades
from main import NUMBER_OF_GRADES, NUMBER_OF_CLASSES, NUMBER_OF_STUDENTS


def connection():
    mydb_con = mysql.connector.connect(
        host="SG-mysqlTest-5329-mysql-master.servers.mongodirector.com",
        user="sgroot",
        password="ZLOK55bfU@Hf8wjp",
        database="school_db")

    return mydb_con


def create_tables():
    cn = connection()
    cur = cn.cursor()

    cur.execute(f"DROP TABLE IF EXISTS classes")
    cur.execute(
        f"CREATE TABLE classes (class_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(255), is_specialized BOOL)"
    )
    cur.execute(f"DROP TABLE IF EXISTS grades")
    cur.execute(
        f"CREATE TABLE grades (grade_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, lang INT(5), math INT(5))"
    )
    cur.execute(f"DROP TABLE IF EXISTS students")
    cur.execute(
        f"CREATE TABLE students (student_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci, grade_id INT, class_id INT)"
    )
    cn.commit()
    cn.close()


def set_foreign_key():
    cn = connection()
    cur = cn.cursor()

    sql = "ALTER TABLE %s ADD FOREIGN KEY (%s) REFERENCES %s (%s)"
    students_grades = (Students.tablename, Students.grade_id, Grades.tablename,
                       Grades.grade_id)
    students_classes = (Students.tablename, Students.class_id,
                        Classes.tablename, Classes.class_id)

    cur.execute(sql % students_grades)
    cur.execute(sql % students_classes)

    cn.commit()
    cn.close()


def create_class(number_of_classes=NUMBER_OF_CLASSES):
    start = timeit.default_timer()

    cn = connection()
    cur = cn.cursor()

    sql = "INSERT INTO classes (name, is_specialized) VALUES (%s, %s)"
    val_list = []
    for i in range(number_of_classes):
        val = (f"K{60 + i%20}{random.choice(string.ascii_letters).upper()}",
               randint(0, 1))
        val_list.append(val)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.connector.Error as err:
        logging.info(err)

    last_class_id = cur.lastrowid

    cn.close()

    stop = timeit.default_timer()  # Stop timer to check time create class dict
    logging.info(
        f'Time created {number_of_classes} classes estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
    )

    return last_class_id


def create_grade(number_of_grades=NUMBER_OF_GRADES):
    start = timeit.default_timer()

    cn = connection()
    cur = cn.cursor()

    sql = "INSERT INTO grades (lang, math) VALUES (%s, %s)"

    val_list = []
    for i in range(number_of_grades):
        val = (randint(0, 10), randint(0, 10))
        val_list.append(val)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.connector.Error as err:
        logging.info(err)

    cn.close()

    stop = timeit.default_timer()  # Stop timer to check time create class dict
    logging.info(
        f'Time created {number_of_grades} grades estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
    )


def create_student(student_id,
                   batch,
                   number_of_class=NUMBER_OF_CLASSES,
                   number_of_students=NUMBER_OF_STUDENTS):
    start = timeit.default_timer()
    cn = connection()
    cur = cn.cursor()

    sql = "INSERT INTO students (student_id, name, grade_id, class_id) VALUES (%s, %s, %s, %s)"

    val_list = []

    first_name, last_name = [], []  # two list to store all names
    NUMBER_OF_FIRST_NAME, NUMBER_OF_LAST_NAME = get_name_list(
        first_name, last_name)

    start_grade_id = batch * NUMBER_OF_GRADES

    for i in range(number_of_students):
        name = get_name(first_name, last_name, NUMBER_OF_FIRST_NAME,
                        NUMBER_OF_LAST_NAME)
        class_id = randint(1, number_of_class)

        val = (student_id + i, name, i + start_grade_id + 1, class_id)
        val_list.append(val)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.connector.Error as err:
        logging.info(err)

    cn.close()
    stop = timeit.default_timer()  # Stop timer to check time create class dict
    logging.info(
        f'Time created {number_of_students} students estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
    )