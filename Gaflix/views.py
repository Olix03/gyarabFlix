from django.http import HttpResponse
from django.template import loader
from Gaflix.models import *


def intro(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'categories': Category.objects.all()}))


def list_movies(request):
    template = loader.get_template('list_movies.html')
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context))


def categories(request, category):
    template = loader.get_template('list_movies.html')
    context = {
        'movies': Movie.objects.filter(category__title=category),
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context))


def list_actors(request):
    template = loader.get_template('list_actor.html')
    context = {
        'actors': Actor.objects.all()
    }
    return HttpResponse(template.render(context))
