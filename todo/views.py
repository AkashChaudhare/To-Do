from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request,'todo/base.html')

class Home(ListView):
    model=Task
    template_name = 'todo/something.html'

class Profile(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'
    ordering=['-completed']
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('completed','-date')

class TaskDetail(UserPassesTestMixin,LoginRequiredMixin,DetailView):
    model=Task
    def test_func(self):
        task=self.get_object()
        if self.request.user==task.user:
            return True
        return False

class TaskCreate(CreateView):
    model=Task
    fields=['title','details']
    success_url=reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class TaskUpdate(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','completed','details']
    
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def test_func(self):
        task=self.get_object()
        if self.request.user==task.user:
            return True
        return False

class TaskDelete(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Task
    success_url='/'
    def test_func(self):
        task=self.get_object()
        if self.request.user==task.user:
            return True
        return False

class Register(SuccessMessageMixin,CreateView):
    form_class=UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    success_message = 'Your account has been created. Please log in to continue'

