from django.shortcuts import render
from .models import Site

def liste_sites(request):
    sites = Site.objects.filter(utilisateur=request.user)
    return render(request, 'gestionnaire/liste_sites.html', {'sites': sites})
