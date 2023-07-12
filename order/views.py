from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddCartForm
from .models import Cart

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