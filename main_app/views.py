from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Game, Note
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

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
    print(notes)
    return render(request, 'games/detail.html', {'game': game, 'notes': notes})


class GameCreate(CreateView):
    model = Game
    fields = ['title']
    
class GameUpdate(UpdateView):
    model = Game
    fields = ['title']
    
class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

class NoteCreate(CreateView):
    model = Note
    fields = ['content', 'game']
    success_url = '/games'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('games')
        else:
            error_message = "Invalid signup - Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)