from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    """
    View the cart summary, if products are added.
    gets information from the Cart class in
    the cart.py.
    inspired from:
    https://www.geeksforgeeks.org/how-to-add-cart-in-a-web-page-using-django/
    """
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(
        request,
        "cart_summary.html",
        {"cart_products": cart_products,
         "quantities": quantities,
         "totals": totals},
    )


def cart_add(request):
    """
    Get the cart And test for POST
    lookup the product from database and save it to a session.
    Updates the cart quantity and return the response.
    inspired from:
    https://www.geeksforgeeks.org/how-to-add-cart-in-a-web-page-using-django/
    """
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({"qty": cart_quantity})
        messages.success(
            request,
            (
                "Product Have Been Added To Your Shooping \
            Cart"
            ),
        )
        return response


def cart_delete(request):
    """
    Delete the chosen product from the cart.
    inspired from:
    https://www.geeksforgeeks.org/how-to-add-cart-in-a-web-page-using-django/
    """
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        cart.delete(product=product_id)
        response = JsonResponse({"product": product_id})
        messages.success(
            request,
            (
                "Product Have Been Removed From The \
            Shooping Cart"
            ),
        )
        return response


def cart_update(request):
    """
    Update the products in the cart if
    qty is updated.
    inspired from:
    https://www.geeksforgeeks.org/how-to-add-cart-in-a-web-page-using-django/
    """
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({"qty": product_qty})
        messages.success(request, ("Your Shooping Cart Have Been Updated"))
        return response
