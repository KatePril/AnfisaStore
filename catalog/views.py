from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category
from ice_cream.models import IceCream
# Create your views here.

class CatalogIndexView(ListView):
    template_name = 'catalog/index.html'
    model = Category

    def get_queryset(self):
        return Category.objects.filter(parent=None)

class IceCreamByCategoryView(ListView):
    template_name = 'catalog/category.html'
    category = None
    categories = Category.objects.all()


    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = IceCream.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = 0
        context['category'] = self.category
        context['categories'] = self.categories
        return context