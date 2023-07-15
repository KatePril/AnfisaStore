from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import AddCartForm
from .models import Cart
from django.views.generic import View

from anfisa.settings import PAGE_NAMES

from django.http import HttpResponse
# Create your views here.
def get_cart_data(user_id):
    cart = Cart.objects.filter(user=user_id)
    total = 0
    for row in cart:
        total += row.ice_cream.price * row.quantity
    return {'cart': cart, 'total': total}

def add_to_cart(request):
    data = request.GET.copy()
    data.update({'user': request.user.id})
    request.GET = data
    form = AddCartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        row = Cart.objects.filter(product=cd['product'], user=cd['user'])
        if row:
            Cart.objects.filter(id = row.id).update(quantity=row.quantity+cd['quentity'])
        else:
            form.save()
        return render(request,
                    'order/added.html',
                    {'product': cd['product'],
                    'cart': get_cart_data(cd['user'])}
                    )       
    else:
        return HttpResponse('ДОРОБИ МЕНЕ!!!')

class AddToCartView(View):
    def get(self, request):
        data = request.GET.copy()
        data.update(user=request.user)
        request.GET = data
        form = AddCartForm(request.GET)
        # print(form)
        # print(form.is_valid())
 
        cd = form.data
        if form.is_valid():
            cd = form.cleaned_data
            print('-'* 100)
            print(cd)
            print('-'* 100)
            row = Cart.objects.filter(ice_cream=cd['ice_cream'], user=cd['user']).first()
            if row:
                Cart.objects.filter(id=row.id).update(quantity=cd['quantity'])
            else:
                form.save()
        return render(request, 'order/added.html', {'ice_cream': cd['object'], 'cart': get_cart_data(cd['user']), 'breadcrumbs': self.get_breadcrumbs()})
        
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        breadcrumbs[reverse('cart')] = 'Кошик'
        breadcrumbs['current'] = 'Додано'
        return breadcrumbs

class CartView(View):
    
    def get(self, request):
        user_id = request.user.id
        return render(request, 'order/cart_list.html', {'cart': get_cart_data(user_id), 'breadcrumbs': self.get_breadcrumbs()})
    
    def get_breadcrumbs(self):
        breadcrumbs = {reverse('catalog'): PAGE_NAMES['catalog']}
        breadcrumbs['current'] = 'Кошик'
        return breadcrumbs