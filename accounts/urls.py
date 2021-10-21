from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]