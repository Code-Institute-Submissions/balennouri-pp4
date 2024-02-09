from .cart import Cart


# Build context prcessor so the cart is working on all the pages.
def cart(request):
    # return the default data from our cart
    return{'cart':Cart(request)}
    