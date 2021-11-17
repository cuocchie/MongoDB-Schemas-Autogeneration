import time
import timeit
from names import get_first_name, get_last_name
from pymongo import MongoClient
import string, random


DB_URI = "mongodb://admin:EVDkyyc4ubS2pa3p@SG-MongTest-47896.servers.mongodirector.com:27017/admin"
# Create Connection
client = MongoClient(DB_URI)

db = client.school_db

students = db.students
classes = db.classes

NUMBER_OF_CLASSES = 2
NUMBER_OF_STUDENTS = 10000

class_list = []

start = timeit.default_timer()

for i in range(NUMBER_OF_CLASSES):
    class_info = {
        "name": f"K{60+i}{random.choice(string.ascii_letters).upper()}",
        "is_specialized": random.randint(0, 1) == 1,
    }
    class_list.append(class_info)

stop = timeit.default_timer()
print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))
start = timeit.default_timer()
class_id = classes.insert_many(class_list).inserted_ids
stop = timeit.default_timer()
print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))
start = timeit.default_timer()

length = len(class_list)
print(length)
student_list = []
for i in range(NUMBER_OF_STUDENTS):
    student_info = {
        "student_id": 19000000 + i,
        "name": f"{get_first_name()} {get_last_name()}",
        "class_id": i % length,
        "grades": {
            "math": random.randint(0, 10),
            "lang": random.randint(0, 10),
        },
    }
    student_list.append(student_info)
stop = timeit.default_timer()
print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))

start = timeit.default_timer()
students.insert_many(student_list, bypass_document_validation=True)
stop = timeit.default_timer()
print("Time estimated: ", time.strftime("%H:%M:%S", time.gmtime(stop - start)))
