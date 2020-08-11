from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    product = Product.objects

    context = {
        'product': product
    }
    return render(request, 'pages/index.html', context)
