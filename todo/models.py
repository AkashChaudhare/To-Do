from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    

    def get_absolute_url(self,):
        return reverse('home')     #redirects to blog-home after saving form
    def __str__(self) -> str:
        return self.title

    
