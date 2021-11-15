from mongoengine.connection import DEFAULT_CONNECTION_NAME
from mongoengine.document import Document
from mongoengine.fields import BooleanField, DateField, IntField, StringField


class Class(Document):
    class_name = StringField(required=True)
    is_specialized = BooleanField(default=False)

    year_start = IntField(required=True, min_value=2000)
    year_end = IntField(required=False, default=None)

    meta = {"db_alias": DEFAULT_CONNECTION_NAME, "collection": "class"}
