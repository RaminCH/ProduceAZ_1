from django.shortcuts import render
from goodsApp.models import *
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView
from django.contrib.auth.models import User
from goodsApp.forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def categories(request):
    return render(request, 'goodsApp/product.html')

def products(request):
    context = {
        'category': Category.objects.all()
    }
    print(context)
    return render(request, 'product.html', context)

# def products(request):
#     page_number = reuqest.GET.get('page', 1)
#     products = Products.objects.all()
#     p = Paginator(products, 1) # how many pages on the page
#         if isinstance(page_number, int) and int(page_number) > p.num_pages:
#             page_number = p.num_pages
    
#     if not page_number.isdigit():
#         page_number = 1
#     elif int(page_number) > p.num_pages:
#         page_number = p.num_pages
#     products_list = p.page(page_number) #p.page(1) 1 shows 1-st page , if we put num 2 shows 2 pages etc
#     print('products', products)
#     context = {
#         'products' = products_list # products
#     }
#     return render(request, 'goodsApp/product.html', context)

def products_detail(request, pk):
    detail = Products.objects.all(id=pk)
    context = {
        'category': detail,
    }
    print(context)
    return render(request, 'product-detail.html', context)







#///////////////////////////////////////////////////////////    

# class ProductDetailView(FormMixin, DetailView):
#     model = Products
#     template_name = "goodsApp/product-detail.html"
#     context_object_name = # ???
#     form_class = # ???

    