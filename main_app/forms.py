from django.forms import ModelForm
from .models import Note, Bachelor


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        
class BachelorCreate(ModelForm):
    class Meta:
        model = Bachelor
        fields = ['name', 'loved', 'liked', 'neutral', 'disliked', 'hated', 'game']