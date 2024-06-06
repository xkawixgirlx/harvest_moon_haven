from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_list, name='index'),
    path('games/<int:game_id>', views.game_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
]