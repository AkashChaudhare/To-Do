# Generated by Django 4.1.5 on 2023-01-27 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]
