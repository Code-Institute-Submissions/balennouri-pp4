from django.shortcuts import redirect, render
from cart.cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def checkout_views(request):
    return render(request, "checkout.html")
