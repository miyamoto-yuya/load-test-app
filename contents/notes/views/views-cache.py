import os
from django.shortcuts import render, redirect
from .db_info import get_db_info
from django.core.cache import cache
from .forms import NoteForm

DB_SERVICE = os.getenv("DB_SERVICE", "RDS")

# モデルの切り替え
if DB_SERVICE == "RDS":
    from .models import Note
elif DB_SERVICE == "DocumentDB":
    from .models import Note
elif DB_SERVICE == "DynamoDB":
    from .models import Note
else:
    raise Exception("Unsupported DB_SERVICE configuration")

def note_list(request):
    notes = cache.get("notes_cache")

    if not notes:
        if DB_SERVICE == "DynamoDB":
            notes = Note.get_all_notes()
        else:
            notes = list(Note.objects.all())
        cache.set("notes_cache", notes, timeout=None)

    db_info = get_db_info()
    return render(request, 'note_list.html', {
        'notes': notes,
        'db_engine': db_info['engine'],
        'db_cluster': db_info['cluster'],
    })

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            if DB_SERVICE == "DynamoDB":
                Note.create_note(title, body)
            else:
                Note(title=title, body=body).save()

            cache.delete("notes_cache")
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def delete_note(request, note_id):
    if DB_SERVICE == "DynamoDB":
        Note.delete(note_id)
    elif DB_SERVICE == "DocumentDB":
        note = Note.objects.get(id=note_id)
        if note:
            note.delete()
    else:
        note = Note.objects.get(id=note_id)
        note.delete()

    cache.delete("notes_cache")  # キャッシュ削除
    return redirect('note_list')
