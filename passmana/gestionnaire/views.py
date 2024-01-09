from django.shortcuts import render, redirect, get_object_or_404
from .forms import SiteForm
from .models import Site
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_sites')
        else:
            return render(request, 'gestionnaire/login.html', {'error': 'Invalid credentials'})
    return render(request, 'gestionnaire/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def ajouter_site(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.utilisateur = request.user
            site.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'gestionnaire/ajouter_site.html', {'form': form})

# Vue pour modifier un site existant
def modifier_site(request, pk):
    site = get_object_or_404(Site, pk=pk, utilisateur=request.user)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm(instance=site)
    return render(request, 'gestionnaire/modifier_site.html', {'form': form})

# Vue pour supprimer un site
def supprimer_site(request, pk):
    site = get_object_or_404(Site, pk=pk, utilisateur=request.user)
    if request.method == "POST":
        site.delete()
        return redirect('liste_sites')
    return render(request, 'gestionnaire/supprimer_site.html', {'site': site})
