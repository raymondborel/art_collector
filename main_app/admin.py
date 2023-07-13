from django.contrib import admin
from .models import Artist, Artwork, Collection # import the Artist model from models.py
# Register your models here.

admin.site.register(Artist) # this line will add the model to the admin panel
admin.site.register(Artwork) # this line will add the model to the admin panel
admin.site.register(Collection) # this line will add the model to the admin panel
# admin.site.register(Artwork) # this line will add the model to the admin panel