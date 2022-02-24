from django.contrib import admin
from Gaflix.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Director)
