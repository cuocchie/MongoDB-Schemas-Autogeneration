from mongoengine import StringField, DateField, Document
from mongoengine.connection import DEFAULT_CONNECTION_NAME
from mongoengine.fields import EmbeddedDocumentField, ListField, ReferenceField
from .contact import Contact


class Student(Document):
    name = StringField(required=True)
    contact = EmbeddedDocumentField(Contact)
    birth = DateField(required=True)
    grade = ListField(ReferenceField("Grade"))
    class_id = ReferenceField("Class")

    meta = {"db_alias": DEFAULT_CONNECTION_NAME, "collection": "students"}
