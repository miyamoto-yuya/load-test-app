from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from .db_info import get_db_info

def note_list(request):
    notes = Note.get_all()
    db_info = get_db_info()
    return render(request, 'note_list.html', {
      'notes': notes,
      'db_engine': db_info['engine'],
      'db_cluster': db_info['cluster'],
    })

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            Note.create(title, body)
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def delete_note(request, note_id):
    Note.delete(note_id)
    return redirect('note_list')

