from django.contrib import admin

from .models import Category,Anime

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['anime_name', 'episodes', 'status']
    list_display_links = list_display

admin.site.register(Category)
