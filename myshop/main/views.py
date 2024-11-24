from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import ProductCategory, Product, Basket
from users.models import User
from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def index(request):
    context = {'title': 'Kickflip Store'}
    return render(request,'main/index.html', context)


def catalog(request):
    context = {
        'title': 'КАТАЛОГ',
        'catalog': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request,"main/cat.html", context)

def contacts(request):
    return render(request,"main/contact.html")

def order_create(request):
    context={
        'title': 'Создание заказа',
    }
    return render(request, "main/order_create.html", context)

class ProductDetaiView(DetailView):
    model = Product
    template_name = 'catalog/work2024.html'
    context_object_name = 'Product'
    extra_context = {'title': 'Детали товара'}

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    selected_size = request.POST.get('size')
    
    basket = Basket.objects.filter(
        user=request.user, 
        product=product,
        selected_size=selected_size
    ).first()

    if basket:
        basket.quantity += 1
        basket.save()
    else:
        Basket.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            selected_size=selected_size
        )

    return HttpResponsePermanentRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponsePermanentRedirect(request.META['HTTP_REFERER'])

