from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from players.models import Player
# Create your views here.

# The members view does the following:

# Creates a myplayers object with all the values of the Player model.
# Loads the players.html template.
# Creates an object containing the myplayers object.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.


def players(request):
    myplayers = Player.objects.all().values()
    template = loader.get_template('players.html')
    context = {
        'myplayers': myplayers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myplayer = Player.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myplayer': myplayer,
    }
    return HttpResponse(template.render(context, request))
