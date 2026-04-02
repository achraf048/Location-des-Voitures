from django.urls import path
from . import views

urlpatterns = [
    path('voiture/<int:id>/', views.voiture_detail, name='voiture_detail'),
]