from django.contrib import admin

# Register your models here.
from .models import *

class ListingAdmin(admin.ModelAdmin):
    list_display=('title','type','year','band','sold')

class BandAdmin(admin.ModelAdmin):
    list_display=('name','year_formed','genre')

admin.site.register(Listing,ListingAdmin)
admin.site.register(Band,BandAdmin)


