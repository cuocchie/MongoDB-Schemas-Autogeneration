from mongoengine.connection import DEFAULT_CONNECTION_NAME
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import DecimalField, DecimalField, StringField, FloatField


class Grade(Document):
    semester_number = StringField(required=True)

    math = DecimalField(default=0, max_value=10, min_value=0, precision=2)
    lang = DecimalField(default=0, max_value=10, min_value=0, precision=2)
    sci = DecimalField(default=0, max_value=10, min_value=0, precision=2)

    meta = {"db_alias": DEFAULT_CONNECTION_NAME, "collection": "grades"}
