from django.urls import path 
from .views import *

app_name = 'goodsApp'

urlpatterns = [
    path('',index,name='index'),#home
    path('products/', products, name='products'), # product.html == catalog???
    path('product_detail/',products_detail, name='product-detail'),
]

