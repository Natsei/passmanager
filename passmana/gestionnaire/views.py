from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Site
from .forms import SiteForm, SignUpForm

@login_required
def liste_sites(request):
    sites = Site.objects.filter(utilisateur=request.user)
    return render(request, 'gestionnaire/liste_sites.html', {'sites': sites})

@login_required
def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.utilisateur = request.user
            site.save()
            return redirect('liste_sites')
    else:
        form = SiteForm()
    return render(request, 'gestionnaire/ajouter_site.html', {'form': form})

@login_required
def modifier_site(request, pk):
    site = get_object_or_404(Site, pk=pk, utilisateur=request.user)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('liste_sites')
    else:
        form = SiteForm(instance=site)
    return render(request, 'gestionnaire/modifier_site.html', {'form': form})

@login_required
def supprimer_site(request, pk):
    site = get_object_or_404(Site, pk=pk, utilisateur=request.user)
    if request.method == "POST":
        site.delete()
        return redirect('liste_sites')
    return render(request, 'gestionnaire/supprimer_site.html', {'site': site})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_sites')
        else:
            return render(request, 'gestionnaire/login.html', {'error': 'Nom d’utilisateur ou mot de passe incorrect'})
    return render(request, 'gestionnaire/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('liste_sites')
    else:
        form = SignUpForm()
    return render(request, 'gestionnaire/register.html', {'form': form})
