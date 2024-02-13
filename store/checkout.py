from django.shortcuts import render


def checkout_views(request):
    return render(request, "checkout.html")
