from django.db import models

# Create your models here.
class Artist(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Artwork(models.Model):

    name = models.CharField(max_length=150)
    image = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.name

class Collection(models.Model):
    title = models.CharField(max_length=150)
    artworks = models.ManyToManyField(Artwork)

    def __str__(self):
        return self.title