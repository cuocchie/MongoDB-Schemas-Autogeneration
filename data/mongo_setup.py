import mongoengine

from mongoengine import connect
from mongoengine.connection import DEFAULT_CONNECTION_NAME

DB_URI = "mongodb+srv://master_user:masteruser@mongodb-test.1dtyg.mongodb.net/school-db"


def global_init():
    connect(host=DB_URI, alias=DEFAULT_CONNECTION_NAME)
