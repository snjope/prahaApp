from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Täällä on teidän nimet ja numerot.")