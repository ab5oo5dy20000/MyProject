from django.shortcuts import render
from .models import Product

# عرض قائمة المنتجات في صفحة مخصصة (store/home.html)
def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'store/home.html', {'products': products})

# عرض الصفحة الرئيسية العامة (home.html) مع تمرير المنتجات إليها
def homepage(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'home.html', {'products': products})
