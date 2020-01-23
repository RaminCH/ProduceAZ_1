from django.shortcuts import render
from goodsApp.models import *
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView
from django.contrib.auth.models import User
from goodsApp.forms import *
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

# def categories(request):
#     return render(request, 'goodsApp/product.html')




#----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------API for jquery drop down------------------------------

def sorting(request, sort_by):
    if request.method == 'POST':
        products = Products.objects.order_by(sort_by)
        product_list = list(products.values('id', 'name', 'price', 'image'))

        return JsonResponse(product_list, safe=False) 

#-----------------------------------------------------------------------------------------------------------------

# **********************************************Products***************************************************
def get_products(request):
    product_list = Products.objects.all()
    if request.is_ajax():
        result = []
        for i in product_list:
            obj = {'name' : i.name}
            result.append(obj)
            
        return JsonResponse({
            'name': result
        })
    
    if request.method == 'POST':
        query = request.POST.get('q')
        product_list = Products.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query) | Q(price__icontains=query) | Q(created_at__icontains=query))


    categories = Category.objects.all()

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    len_product = product_list.count()
    page_num = products.number 
    start =  (page_num - 1) * 6 + 1
    end = 6 * page_num
    if end > len_product:
        end = len_product

    context = {
        'categories': categories,
        'products': products,
        'len_product': len_product,
        'start': start,
        'end': end,
    }

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
# ----------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------Categories----------------------------------------
def get_category(request, cat_id):
    categories = Category.objects.all()
    product_list = Products.objects.filter(category__id = cat_id)

    if request.method == 'POST': # for searching field in categories
        query = request.POST.get('q')
        product_list = Products.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query) | Q(price__icontains=query) | Q(created_at__icontains=query))

    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    len_product = product_list.count()
    page_num = products.number 
    start =  (page_num - 1) * 6 + 1
    end = 6 * page_num
    if end > len_product:
        end = len_product

    context = {
        'cat_id': cat_id,
        'categories': categories,
        'products': products,
        'len_product': len_product,
        'start': start,
        'end': end,
    }
    
    return render(request, 'product.html', context)

#---------------------------------------------------------Detail Of Product ---------------------------------------
def get_detail(request, prod_id):
    product = Products.objects.get(id = prod_id)           
    related_products = Products.objects.filter(category = product.category)
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'product-detail.html', context)
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------Search Result-----------------------------------------

# class SearchResultsView(ListView):
#     model = Products
#     template_name = 'product.html'

#     def get_queryset(self):
#         query = self.request.GET.get('q') # q is the user's search query
#         object_list = Products.objects.filter(
#             Q(name__icontains=query) | Q(price__icontains=query | Q(category__icontains=query | Q(created_at__icontains=query | Q(created_at__icontains=query)
#         )
#         context = {
#             'object_list': object_list 
#         }
#         return render(request, 'product.html', context)
       

# def search_products(request):
#     query = request.GET.get('q')
#     print(query)
#     object_list = Products.objects.filter(Q(name__icontains=query) | Q(price__icontains=query) | Q(category__icontains=query) | Q(created_at__icontains=query) | Q(created_at__icontains=query))
#     context = {
#         'object_list': object_list 
#     }
#     return render(request, 'product.html', context)
#------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------Experiments------------------------------------------
# Paginator function got form internet
#------------------------------------------------------------------------
# def listing(request):
#     contact_list = Products.objects.all()
#     paginator = Paginator(contact_list, 5) # Show 5 products per page.

#     page_number = request.GET.get('products')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'products.html', {'page_obj': page_obj})
#------------------------------------------------------------------------   



#///////////////////////////////////////////////////////////    

# -------------------------------------------------------------------------Class Base of a Detail Product Page ----


# class SingleRecipeView(FormMixin, DetailView): # Single-nin class base-i
#     model = Products
#     template_name = "goodsApp/product-detail.html"

#     # def get_queryset(self, request, *args, **kwargs):

#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset)
#         obj.view_count = obj.view_count + 1
#         obj.save()
#         return obj
    

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.replied_comment = request.POST.get('reply_comment')
#         form = self.get_form()
#         # form.save(commit=False)
#         if form.is_valid():
#             print('here')
#             return self.form_valid(form)
#         else:
#             print('here 2')
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         comment = form.save(commit=False)
#         comment.user = self.request.user
#         comment.recipe = self.object
#         if not self.replied_comment is None and self.replied_comment.isdigit():
#             r_comment = Comment.objects.get(id=int(self.replied_comment))
#             comment.reply_comment = r_comment 
#         comment.save()
#         self.success_url = reverse_lazy('stories:single', kwargs=
#         {'pk': self.object.id})
#         return super().form_valid(form)

    
