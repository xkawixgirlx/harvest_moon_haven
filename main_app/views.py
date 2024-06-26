from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Game, Note, Bachelor, Bachelorette
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import NoteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    notes = Note.objects.filter(game=game_id)
    return render(request, 'games/detail.html', {'game': game, 'notes': notes})



class GameCreate(CreateView, LoginRequiredMixin):
    model = Game
    fields = ['title']
    
class GameUpdate(UpdateView, LoginRequiredMixin):
    model = Game
    fields = ['title']
    
class GameDelete(DeleteView, LoginRequiredMixin):
    model = Game
    success_url = '/games'



@login_required
def note_create(request, game_id):
    form = NoteForm(request.POST, use_required_attribute=False)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.user = request.user
        new_note.game_id = game_id
        new_note.save()
        return redirect('detail', game_id)    
    return render(request,'main_app/note_form.html', {'form': form})
        
 

class NoteUpdate(UpdateView, LoginRequiredMixin):
    model = Note
    fields = ['title', 'content']
    template_name = 'main_app/note_update_form.html' 
    
    def get_success_url(self):
        return f"/games/{self.object.game.id}"   

class NoteDelete(DeleteView, LoginRequiredMixin):
    model = Note
    
    def get_success_url(self):
        return f"/games/{self.object.game.id}"



@login_required
def my_notes(request):
    notes = Note.objects.filter(user=request.user)
    games = Game.objects.all()
    bachelors = Bachelor.objects.all()
    bachelorettes = Bachelorette.objects.all()
    return render(request, 'notes/index.html', {'notes': notes, 'games': games, 'bachelors': bachelors, 'bachelorettes': bachelorettes})



def all_bachelors(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'bachelor/index.html', {'game': game})

class BachelorCreate(CreateView, LoginRequiredMixin):
    model = Bachelor
    fields = ['name', 'loved', 'liked', 'neutral', 'disliked', 'hated', 'game']
    
    def get_success_url(self):
        return f'/games/{self.object.game.id}/all_bachelors'
    
class BachelorDetail(DetailView):
    model = Bachelor
    
class BachelorUpdate(UpdateView, LoginRequiredMixin):
    model = Bachelor
    fields = ['name', 'loved', 'liked', 'neutral', 'disliked', 'hated', 'game']
    template_name = 'main_app/bachelor_update_form.html'
    
    def get_success_url(self):
        return f"/games/{self.object.game.id}/all_bachelors"

class BachelorDelete(DeleteView, LoginRequiredMixin):
    model = Bachelor
    success_url = '/games/{game_id}/all_bachelors'
   
   
    
@login_required
def bachelor_createnote(request, bachelor_id):
    form = NoteForm(request.POST)
    bachelor = Bachelor.objects.get(id=bachelor_id)
    if form.is_valid():
        new_bachelor_note = form.save(commit=False)
        new_bachelor_note.user = request.user
        new_bachelor_note.bachelor_id = bachelor_id
        new_bachelor_note.game_id = bachelor.game_id
        new_bachelor_note.save()
        return redirect('bachelor_detail', bachelor_id)    
    return render(request,'main_app/note_form.html', {'form': form})



def all_bachelorettes(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'bachelorette/index.html', {'game': game})
  
  
  
class BacheloretteCreate(CreateView, LoginRequiredMixin):
    model = Bachelorette
    fields = ['name', 'loved', 'liked', 'neutral', 'disliked', 'hated', 'game']
    
    def get_success_url(self):
        return f'/games/{self.object.game.id}/all_bachelorettes'
    
class BacheloretteDetail(DetailView):
    model = Bachelorette
    
class BacheloretteUpdate(UpdateView, LoginRequiredMixin):
        model = Bachelorette
        fields = ['name', 'loved', 'liked', 'neutral', 'disliked', 'hated', 'game']

        def get_success_url(self):
            return f'/games/{self.object.game.id}/all_bachelorettes'

class BacheloretteDelete(DeleteView, LoginRequiredMixin):
    model = Bachelorette
    success_url = '/games/{game_id}/all_bachelorettes'
  
  
  
@login_required
def bachelorette_createnote(request, bachelorette_id):
    form = NoteForm(request.POST)
    bachelorette = Bachelorette.objects.get(id=bachelorette_id)
    if form.is_valid():
        new_bachelorette_note = form.save(commit=False)
        new_bachelorette_note.user = request.user
        new_bachelorette_note.bachelorette_id = bachelorette_id
        new_bachelorette_note.game_id = bachelorette.game_id
        new_bachelorette_note.save()
        return redirect('bachelorette_detail', bachelorette_id)    
    return render(request,'main_app/note_form.html', {'form': form})



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid signup - Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)