from django.contrib import admin
from .models import BoyBand # import the Artist model from models.py
# Register your models here.

admin.site.register(BoyBand) # this line will add the model to the admin panel