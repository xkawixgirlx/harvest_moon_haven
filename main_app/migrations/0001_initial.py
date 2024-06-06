# Generated by Django 5.0.6 on 2024-06-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('notes', models.TextField(max_length=500)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]