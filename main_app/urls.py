from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_list, name='index'),
    path('games/create', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),
    path('games/<int:game_id>', views.game_detail, name='detail'),
    path('games/<int:game_id>/create_note', views.note_create, name='create_note'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('accounts/signup/', views.signup, name='signup'),
]