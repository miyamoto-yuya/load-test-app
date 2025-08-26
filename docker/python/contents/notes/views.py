from django.shortcuts import render, redirect
from .db_info import get_db_info
from .models import Note
from .forms import NoteForm

def note_list(request):
   notes = list(Note.objects.all())
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
            Note(title=form.cleaned_data['title'], body=form.cleaned_data['body']).save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('note_list')

