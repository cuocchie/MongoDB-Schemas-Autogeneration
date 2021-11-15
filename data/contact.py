from mongoengine import EmbeddedDocument
from mongoengine.fields import EmailField, StringField


class Contact(EmbeddedDocument):
    phone = StringField()
    email = EmailField(required=True)
