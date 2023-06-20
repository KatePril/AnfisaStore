from django.shortcuts import render, get_object_or_404

from .models import IceCream

def index(request):
    template = 'ice_cream/index.html'
    selected_ice_creams = IceCream.objects.filter(on_main='True')
    # только то мороженое, у кторого есть флаг on_main
    context = {
        'selected_ice_creams': selected_ice_creams,
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/ice_cream_list.html'
    ice_creams = IceCream.objects.all()
    # все мороженое
    context = {
        'ice_creams': ice_creams,
    }
    return render(request, template, context)


def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    ice_cream = get_object_or_404(IceCream, id=pk)
    # Мороженое с id из запроса
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context)

