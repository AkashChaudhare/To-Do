# Generated by Django 4.1.5 on 2023-01-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_task_task_task_details_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]