import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations = []
    page_number = int(request.GET.get("page", 1))
    with open(settings.BUS_STATION_CSV, "r", encoding="utf-8", newline="") as f:
        dict_reader = csv.DictReader(f)
        for station in dict_reader:
            stations.append(station)
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
