from django.contrib import admin
from Gaflix.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthdate', 'sex']
    search_fields = ['name']
    list_filter = ['sex']
    list_editable = ['birthdate', 'sex']
    date_hierarchy = "birthdate"


# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor, ActorAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Director)
