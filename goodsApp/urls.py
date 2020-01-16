from django.urls import path 
from .views import *

app_name = 'goodsApp'

urlpatterns = [
    path('',index,name='index'),#home
    path('products/', get_products, name='products'), 
    path('products/<int:cat_id>', get_category, name='get_category'),
    path('products_detail/<int:prod_id>', get_detail, name='get_detail'),
    # path('search/', search_products, name='search_results'),
]

