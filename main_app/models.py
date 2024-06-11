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


class Bachelor(models.Model):
    loved = models.TextField(max_length=100)
    liked = models.TextField(max_length=100)
    neutral = models.TextField(max_length=100)
    disliked = models.TextField(max_length=100)
    hated = models.TextField(max_length=100)
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True, related_name='bachelors')

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('bachelors', kwargs={'bachelors_id': self.id})

    
class Bachelorette(models.Model):
    loved = models.TextField(max_length=100)
    liked = models.TextField(max_length=100)
    neutral = models.TextField(max_length=100)
    disliked = models.TextField(max_length=100)
    hated = models.TextField(max_length=100)
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True, related_name='bachelorettes')
    
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('bachelorettes', kwargs={'bachelorettes_id': self.id})



class Note(models.Model):
    title = models.CharField(max_length=100, default='null')
    content = models.TextField(max_length=3500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='notes', on_delete=models.CASCADE)
    bachelors = models.ForeignKey(Bachelor, on_delete=models.CASCADE, blank=True, null=True)
    bachelorettes = models.ForeignKey(Bachelorette, on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.content}, {self.updated_at}' 
    
    class Meta:
        ordering = ['-updated_at']   
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'note_id': self.id})


