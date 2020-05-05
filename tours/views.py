from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from data import *

# context['loop_times'] = range(1, 8)

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={
                'tours': tours,
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
            }
        )

class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/departure.html', context={
                'tours': tours,
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
            }
        )

class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/tour.html', context={
                'tours': tours,
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
            }
        )