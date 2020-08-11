from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            print("title ---- {}".format(product.title))
            product.desscription = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.urls = request.POST['url']
            else:
                product.urls = 'http://' + request.POST['url']

            product.icon = request.FILES['icon']
            print("icon ---- {}".format(product.icon))
            product.image = request.FILES['image']
            print("image ---- {}".format(product.image))
            product.created_date = timezone.datetime.now()
            print("created_date ---- {}".format(product.created_date))
            product.Hunter = request.user
            print("hunter ---- {}".format(product.Hunter))
            product.save()
            print("Product Saved")
            messages.success(request, 'Your Product has been Published')
            print("Redirected at index to user --- {}".format(product.Hunter))
            return redirect('/products/' + str(product.id))

        else:
            messages.error(request, 'Please add all the Fields')
            print("Please add all the Fields")
            return redirect('create')
    else:

        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/details.html', context)


@login_required(login_url='/accounts/login/')
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.vote_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
