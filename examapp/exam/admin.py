from django.contrib import admin
from .models import Musician

@admin.register(Musician)
class MusicainAdmin(admin.ModelAdmin):
    """
    튜플, 리스트 둘다 가능
    """
    list_display=["id","name","instrumnet"]
    list_display_links=["name"]
    search_fields=["instrumnet"]
