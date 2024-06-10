from django.contrib import admin
from .models import Game, Note, Bachelor, Bachelorette 

# Register your models here.
admin.site.register(Game)
admin.site.register(Note)
admin.site.register(Bachelor)
admin.site.register(Bachelorette)