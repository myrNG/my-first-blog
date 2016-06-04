from django.db import models

# Create your models here.
from django.utils import timezone # Permet d'importer des morceaux d'autres fichiers

class Post(models.Model):
    author = models.ForeignKey('auth.User') # Lien vers un autre modèle
    title = models.CharField(max_length=200) # Définit un champ de texte avec ici un nombre max de caractères (200)
    text = models.TextField() # Définit un champ de texte sans limite de caractères
    created_date = models.DateTimeField( # Définit le champ en question comme une date ou une heure
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title