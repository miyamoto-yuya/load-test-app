from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from notes.models import Note

@receiver(post_save, sender=Note)
@receiver(post_delete, sender=Note)
def clear_cache(sender, **kwargs):
    cache.delete("notes_list")