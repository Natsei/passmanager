from django.shortcuts import render, redirect, get_object_or_404
from .forms import SiteForm
from .models import Site

# Vue pour ajouter un nouveau site
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
