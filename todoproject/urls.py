from django.contrib import admin
from django.urls import path,include
from todo import views as todo_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',todo_views.index,name='base'),
    path('task/<int:pk>',todo_views.TaskDetail.as_view(),name='detail'), #
    path('task/create/',todo_views.TaskCreate.as_view(),name='create'), #
    path('task/delete/<int:pk>',todo_views.TaskDelete.as_view(),name='delete'), #
    path('task/update/<int:pk>',todo_views.TaskUpdate.as_view(),name='update'), #
    path('login/',auth_views.LoginView.as_view(template_name='todo/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='todo/logout.html'),name='logout'),
    path('register/',todo_views.Register.as_view(template_name='todo/register.html'),name='register'),
    path('',todo_views.Profile.as_view(),name='profile'),
    #path('',todo_views.Home.as_view(),name='home')
]
