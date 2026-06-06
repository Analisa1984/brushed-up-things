from django.contrib import admin
from .models import Artist, Artwork


# Register your models here.
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'price',
        'is_sold',
        'created_at'
        )
    list_filter = ('is_sold', 'artist', 'medium')
    search_fields = ('title', 'description')
    actions = ['mark_as_sold', 'mark_as_available']

    def mark_as_sold(self, request, queryset):
        queryset.update(is_sold=True)
    mark_as_sold.short_description = "Mark selected artworks as Sold"

    def mark_as_available(self, request, queryset):
        queryset.update(is_sold=False)
    mark_as_available.short_description = "Mark selected artworks as Available"
