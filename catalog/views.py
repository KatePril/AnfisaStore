from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category
from ice_cream.models import IceCream
from django.core.paginator import Paginator

from order.views import get_cart_data
from django.urls import reverse

from anfisa.settings import PAGE_NAMES
# Create your views here.
from main.mixins import ListViewBreadcrumbMixin

def get_page_ice_cream(request, articles, pages_num):
    paginator = Paginator(articles, pages_num)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

class CatalogIndexView(ListViewBreadcrumbMixin):
    template_name = 'catalog/index.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
    def get_queryset(self):
        return Category.objects.filter(parent=None)
    
    def get_breadcrumbs(self):
        self.breadcrumbs = {
            'current' : PAGE_NAMES['catalog'],
        } # вказуємо поточну сторінку ДОПИСАТИ
        return self.breadcrumbs

class IceCreamByCategoryView(ListViewBreadcrumbMixin):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()


    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = IceCream.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = self.categories
        context['cart'] = get_cart_data(self.request.user.id)
        return context
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        if self.category.parent:
            linkss = []
            parent = self.category.parent
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
        breadcrumbs.update({'current': self.category.name})
        return breadcrumbs