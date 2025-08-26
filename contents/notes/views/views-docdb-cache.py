from django.core.cache import cache
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note


def note_list(request):
    cache_key = "notes_list"  # キャッシュキー
    notes = cache.get(cache_key)  # キャッシュから取得

    if notes is None:  # キャッシュがない場合
        notes = list(Note.objects.all())
        cache.set(cache_key, notes, timeout=60)

    return render(request, 'note_list.html', {'notes': notes})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            Note(title=form.cleaned_data['title'], body=form.cleaned_data['body']).save()
            cache.delete("notes_list")
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    cache.delete("notes_list")
    return redirect('note_list')

