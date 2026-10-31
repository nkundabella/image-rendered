from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='list'),
    path('delete/<int:pk>/', views.photo_delete, name='delete'),
]
