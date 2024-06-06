from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date



# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=150)
    notes = models.TextField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

     