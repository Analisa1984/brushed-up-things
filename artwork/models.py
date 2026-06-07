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
    MEDIUM_CHOICES = [
        ('Oil on Canvas', 'Oil on Canvas'),
        ('Watercolor', 'Watercolor'),
        ('Sculpture', 'Sculpture'),
        ('Drawings', 'Drawings'),
    ]
    artist = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
        related_name='artworks')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='gallery/', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def is_available(self):
        return not self.is_sold
