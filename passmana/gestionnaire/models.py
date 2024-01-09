from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Site(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    url = models.URLField()
    identifiant = models.CharField(max_length=100)
    mot_de_passe_hash = models.CharField(max_length=128)

    def set_mot_de_passe(self, raw_password):
        self.mot_de_passe_hash = make_password(raw_password)

    def check_mot_de_passe(self, raw_password):
        return check_password(raw_password, self.mot_de_passe_hash)

    def __str__(self):
        return self.nom
