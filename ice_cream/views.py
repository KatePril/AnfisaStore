from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import IceCream


class IceCreamIndex(ListView):
    model = IceCream
    queryset = IceCream.objects.filter(on_main='True')
    template_name = 'ice_cream/icecream_index.html'

class IceCreamList(ListView):
    model = IceCream
    template_name = 'templates/ice_cream/icecream_list.html'
    
class IceCreamDetail(DetailView):
    model = IceCream