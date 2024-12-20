from django.db import models
from django.contrib.auth.models import AbstractUser

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to="user_images/", blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    def __str__(self):
        return self.username


class Store(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="stores")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to="product_images/", blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True, related_name="products"
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    stock = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def is_in_stock(self):
        return self.stock > 0


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name} in {self.city.name if self.city else 'no city'}"
