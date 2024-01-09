from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionnaire/', include('gestionnaire.urls')),
    # Vous pouvez ajouter d'autres chemins globaux ici
]
