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
    path('notes/', views.my_notes, name='notes_index'),
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='delete_note'),
    path('games/<int:game_id>/all_bachelors', views.all_bachelors, name='bachelors'),
    path('bachelor/create', views.BachelorCreate.as_view(), name='bachelor_create'),
    path('bachelor/<int:pk>/update/', views.BachelorUpdate.as_view(), name='bachelor_update'),
    path('bachelor/<int:pk>/delete/', views.BachelorDelete.as_view(), name='bachelor_delete'),
    path('games/<int:game_id>/all_bachelorettes', views.all_bachelorettes, name='bachelorettes'),
    path('bachelorette/<int:pk>/', views.BacheloretteDetail.as_view(), name='bachelorette_detail'),
    path('bachelorette/create_bachelorette', views.BacheloretteCreate.as_view(), name='bachelorette_create'),
    path('bachelorette/<int:pk>/update/', views.BacheloretteUpdate.as_view(), name='bachelorette_update'),
    path('bachelorette/<int:pk>/delete/', views.BacheloretteDelete.as_view(), name='bachelorette_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]