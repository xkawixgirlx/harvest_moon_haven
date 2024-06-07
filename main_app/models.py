from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date



# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})


class Note(models.Model):
    title = models.CharField(max_length=100, default='null')
    content = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='notes', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.content}, {self.updated_at}' 
    
    class Meta:
        ordering = ['-updated_at']   
    
    def get_absolute_url(self):
        print(self)
        return reverse('detail', kwargs={'note_id': self.id})
