from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator
# Create your models here.

class Album(models.Model):
    title = models.CharField()
    artist = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(null=True, blank=True)
    tracks = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.name