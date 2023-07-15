from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import IceCream

from order.views import get_cart_data
from main.mixins import DetailViewBreadcrumbMixin

from django.urls import reverse

from anfisa.settings import PAGE_NAMES

class IceCreamIndex(ListView):
    model = IceCream
    queryset = IceCream.objects.filter(on_main='True')
    template_name = 'ice_cream/icecream_index.html'

class IceCreamList(ListView):
    model = IceCream
    template_name = 'templates/ice_cream/icecream_list.html'
    
class IceCreamDetail(DetailViewBreadcrumbMixin):
    model = IceCream
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        category = self.object.main_category()
        if category:
            if category.parent:
                linkss = []
                parent = category.parent
                while parent is not None:
                    linkss.append(
                        (
                            reverse('category', kwargs={'slug': parent.slug}),
                            parent.name
                        )
                    )
                    parent = parent.parent
                for url, name in linkss[::-1]:
                    breadcrumbs[url] = name
                    #breadcrumbs.update({url: name}) # або так
            breadcrumbs.update({reverse('category', kwargs={'slug': category.slug}): category.name})
        breadcrumbs.update({'current': self.object.name})
        return breadcrumbs