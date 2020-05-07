from django.shortcuts import render
from django.http import Http404
from django.views import View
from data import *
import random


class MainView(View):
    def get(self, request, *args, **kwargs):
        random_items = []
        index_tours = {}
        random_items = random.sample(tours.keys(), 6)
        for i in random_items:
            index_tours[i] = tours[i]
        return render(
            request, 'tours/index.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
                'index_tours': index_tours,
            }
        )


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        departure_value_tours = 0
        current_departures_dict = {}
        price_list = []
        nights_list = []
        if departure not in departures:
            raise Http404
        else:
            for key, value in tours.items():
                if value['departure'] == departure:
                    departure_value_tours = departure_value_tours + 1
                    current_departures_dict[key] = value
            departure = departures[departure]
        for item in current_departures_dict:
            price_list.append(current_departures_dict[item]['price'])
            nights_list.append(current_departures_dict[item]['nights'])
        price_list.sort()
        nights_list.sort()
        return render(
            request, 'tours/departure.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departures': departures,
                'departure': departure,
                'departure_value_tours': departure_value_tours,
                'current_departures_dict': current_departures_dict,
                'price_list': price_list,
                'nights_list': nights_list,
            }
        )


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        if id not in tours:
            raise Http404
        else:
            tour = tours[id]
            departure = departures[tour['departure']]
            return render(
                request, 'tours/tour.html', context={
                    'title': title,
                    'subtitle': subtitle,
                    'description': description,
                    'departure': departure,
                    'tour': tour,
                    'departures': departures,
                }
            )
