from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductForm
from .models import Product

# Create your views here.


def Add_Product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/product')
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form' : form})

def All_Product(request):
    product_s = Product.objects.all()
    return render(request, 'products.html', {'product_s' : product_s})

