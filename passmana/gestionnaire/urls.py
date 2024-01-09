from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.liste_sites, name='liste_sites'),
]
