# Generated by Django 5.0.6 on 2024-06-07 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_note_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='main_app.game'),
        ),
    ]