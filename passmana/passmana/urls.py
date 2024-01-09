from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionnaire/', include('gestionnaire.urls')),
    path('', lambda request: redirect('sites/', permanent=False)),
]
