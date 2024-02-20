from .cart import Cart


def cart(request):
    """
    Build context prcessor so the cart is working on all the pages.
    inspired from:
    https://dev.to/sarahhudaib/context-processors-in-django-15h2
    """
    return {"cart": Cart(request)}
