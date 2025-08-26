import datetime
from uuid import uuid4
from django_mongoengine import Document, fields

class Note(Document):
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    title = fields.StringField(max_length=255)
    body = fields.StringField()

    def __str__(self):
        return self.title

    @staticmethod
    def create(title, body):
        note_id = str(uuid4())
        Note.table.put_item(
            Item={'id': note_id, 'title': title, 'body': body}
        )
        return note_id

    @staticmethod
    def get_all():
        response = Note.table.scan()
        return response.get('Items', [])

    @staticmethod
    def delete(note_id):
        Note.table.delete_item(Key={'id': note_id})
