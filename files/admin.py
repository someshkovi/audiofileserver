from django.contrib import admin

# Register your models here.
from files.models import Podcast, Song

admin.site.register(Podcast)

admin.site.register(Song)