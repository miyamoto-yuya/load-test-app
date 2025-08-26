from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @staticmethod
    def create(title, body):
        note = Note.objects.create(title=title, body=body)
        return note.id

    @staticmethod
    def get_all():
        return list(Note.objects.all().values())
