from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.photo_list, name='list'),
    path('photo/<int:pk>/', views.photo_detail, name='detail'),
    path('photo/<int:pk>/delete/', views.photo_delete, name='delete'),
]
