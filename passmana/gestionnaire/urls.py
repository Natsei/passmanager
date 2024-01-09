from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.liste_sites, name='liste_sites'),
    path('ajouter/', views.ajouter_site, name='ajouter_site'),
    path('modifier/<int:pk>/', views.modifier_site, name='modifier_site'),
    path('supprimer/<int:pk>/', views.supprimer_site, name='supprimer_site'),
]
