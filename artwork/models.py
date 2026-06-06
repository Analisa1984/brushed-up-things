from django.db import models

# Create your models here.


class Artist(models.Model):
    '''Information about the artist'''
    name = models.CharField(max_length=60, unique=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artists/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    '''Information about the artwork pieces'''
    artist = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
        related_name='artworks')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    medium = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        return not self.is_sold
