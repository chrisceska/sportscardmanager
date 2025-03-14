from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('card/<int:pk>/', views.card_detail, name='card_detail'),
    path('card/new/', views.card_create, name='card_create'),
    path('card/<int:pk>/edit/', views.card_edit, name='card_edit'),
    path('card/<int:pk>/delete/', views.card_delete, name='card_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
]
