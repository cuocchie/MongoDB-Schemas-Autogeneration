from datetime import datetime
import time
import timeit
from get_random_name import get_name, get_name_list
from pymongo import MongoClient
import string, random
import logging

# connect to log file to record time, error while inserting
logging.basicConfig(filename='logging.log', level=logging.DEBUG)

# DB_URI - connection address of database
DB_URI = "mongodb://admin:EVDkyyc4ubS2pa3p@SG-MongTest-47896.servers.mongodirector.com:27017/admin"

# Create Connection
client = MongoClient(DB_URI)

# Create db instance
db = client.school_db

# Create student Collection and classes Collection
students = db.students
classes = db.classes

# Number of classes and students
NUMBER_OF_CLASSES = 1000
NUMBER_OF_STUDENTS = 1000000  # per batch

class_list = []  # class_list to store class that be inserted to db later on

start = timeit.default_timer()  # Start timer to check time create class dict

# Create class
for i in range(NUMBER_OF_CLASSES):
    class_info = {
        "name":
        f"K{60+i}{random.choice(string.ascii_letters).upper()}",  # K61T
        "is_specialized": random.randint(0, 1) == 1,  # True/False
    }
    class_list.append(class_info)

stop = timeit.default_timer()  # Stop timer to check time create class dict
logging.info(
    f'Time created {NUMBER_OF_CLASSES} classes estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
)

start = timeit.default_timer(
)  # Start timer to check time insert class document

class_id = classes.insert_many(
    class_list).inserted_ids  # Insert and get all class document _id
stop = timeit.default_timer()  # Stop timer to check time inser class document
logging.info(
    f'Time inserted {NUMBER_OF_CLASSES} classes estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
)

first_name, last_name = [], []  # two list to store all names
NUMBER_OF_FIRST_NAME, NUMBER_OF_LAST_NAME = get_name_list(
    first_name, last_name)

BATCHES = 100  # Number of batches -> total student = 1.000.000 students per batch * 100 batches = 100.000.000 students

for batch in range(BATCHES):
    try:
        start = timeit.default_timer(
        )  # Start timer to check time create 1.000.000 students dict

        logging.info(
            f'\n\n STARTING BATCH {batch}: TIME START = {datetime.now()}')
        student_list = []
        for i in range(NUMBER_OF_STUDENTS):
            student_info = {
                "student_id":
                19000000 + i,
                "name":
                get_name(first_name, last_name, NUMBER_OF_FIRST_NAME,
                         NUMBER_OF_LAST_NAME),
                "class_id":
                class_id[i % NUMBER_OF_CLASSES],
                "grades": {
                    "math": random.randint(0, 10),
                    "lang": random.randint(0, 10),
                },
            }
            student_list.append(student_info)
        stop = timeit.default_timer(
        )  # Stop timer to check time create 1.000.000 students dict
        logging.info(
            f'Time created {NUMBER_OF_STUDENTS} students estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
        )

        start = timeit.default_timer(
        )  # Start timer to check time insert 1.000.000 students documents
        students.insert_many(student_list, bypass_document_validation=True)
        stop = timeit.default_timer(
        )  # Stop timer to check time insert 1.000.000 students documents
        logging.info(
            f'Time inserted {NUMBER_OF_STUDENTS} students estimated: {time.strftime("%H:%M:%S", time.gmtime(stop - start))}'
        )
        logging.info(f'FINISH BATCH {batch}. TIME FINISHED: {datetime.now()}')
    except Exception as e:
        """
        Exception to prevent loop canceled by error (network)
        """
        logging.info('error: ', e)
        time.sleep(100)
        logging.error(f'Batch {batch} failed, increase BATCHES to one')
