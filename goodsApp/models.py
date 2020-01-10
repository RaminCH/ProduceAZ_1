from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=255, blank=False, null=True)
    # product_id = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='product', null=True)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ('-created_at',)


class Products(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=255, blank=False, null=True)
    image = models.ImageField(upload_to='categories')
    price = models.FloatField()
    contact = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=60, blank=False, null=True)
    made_in = models.CharField(max_length=255, blank=False, null=True)
    url = models.CharField(max_length=255, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=True)
    add_info = models.CharField(max_length=255, blank=False, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ('-created_at',)


# Types
# class Order(models.Model):
#     cart = models.ForeignKey(Cart)
#     add_date = models.DateTimeField(auto_now_add=True)
#     order_number = models.IntegerField()
#     enable = models.BooleanField(default=True