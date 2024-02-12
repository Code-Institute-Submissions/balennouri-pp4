from store.models import Product


class Cart:
    def __init__(self, request):
        """
        Gets the current session key if it exists,
        If the user is new user wint have a session key,
        Makes sure cart is available on all pages of site
        """
        self.session = request.session
        cart = self.session.get("session_key")
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
            self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sales:
                        total = total + (product.sales_price * value)
                else:
                    total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        """
        Gets the Ids from the cart,
        From the Id that is taken, use it to lookup the product in
        the database,
        Return the products that was looked up.
        """
        product_ids = self.cart.keys()
        product = Product.objects.filter(id__in=product_ids)
        return product

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        """
        Gets the products in the cart
        and update the cart qty
        """
        product_id = str(product)
        product_qty = int(quantity)
        mycart = self.cart
        mycart[product_id] = product_qty
        self.session.modified = True
        balls = self.cart
        return balls

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
