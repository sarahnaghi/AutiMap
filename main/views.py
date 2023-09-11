from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from centers.models import Center




# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/home.html")


def how_to_start_view(request: HttpRequest):

    return render(request, "main/how_to_start.html")


def having_doubts_view(request: HttpRequest):

    return render(request, "main/having_doubts.html")



def family_journeys_view(request: HttpRequest):

    return render(request, "main/family_journeys.html")