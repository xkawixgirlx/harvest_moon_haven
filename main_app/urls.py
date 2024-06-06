from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_list, name='index'),
    path('games/create', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:game_id>', views.game_detail, name='detail'),
    path('games/<int:game_id>/add_note', views.add_note, name='add_note'),
    path('accounts/signup/', views.signup, name='signup'),
]