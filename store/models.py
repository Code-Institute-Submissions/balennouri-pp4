from django.db import models
import datetime
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model for category, in the admin panel
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    Model for customer, in the admin panel
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    """
    Model for products, in the admin panel
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default="", blank=True, null=True)
    image = CloudinaryField("image", default="placeholder")
    is_sales = models.BooleanField(default=False)
    sales_price = models.DecimalField(
        default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model for order, in the admin panel.
    Did not use, save the function for future development.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


class Comment(models.Model):
    """
    Model for comments, in the admin panel
    """

    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE
    )
    commenter_name = models.CharField(max_length=200)
    commenter_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.product.name, self.commenter_name)
