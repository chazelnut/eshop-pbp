from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
        'class' : 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        }
    return render(request, 'product_detail.html', context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get('filter', 'all')

    if filter_type == 'my':
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")
def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       json_data = serializers.serialize("json", product_item)
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return HttpResponse(b'CREATED', status=201)
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # 🟢 penting banget: ini yang ngisi last_login
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('main:show_main')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False}, status=400)
            messages.error(request, 'Username atau password salah!')
    return render(request, 'login.html')

def logout_user(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        logout(request)
        response = HttpResponse(b'OK', status=200)
        response.delete_cookie('last_login')
        return response
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@require_POST
def add_product_ajax(request):
    if not request.user.is_authenticated:
        return HttpResponse(b'UNAUTHORIZED', status=401)
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price') or 0
    stock = request.POST.get('stock') or 0
    category = request.POST.get('category')
    thumbnail = request.POST.get('thumbnail')
    is_featured = request.POST.get('is_featured') in ['true','True','on','1','checked']
    user = request.user

    new_product = Product(
        name=name,
        description=description,
        price=int(price) if price else 0,
        stock=int(stock) if stock else 0,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()
    return HttpResponse(b'CREATED', status=201)


@require_POST
def update_product_ajax(request, id):
    if not request.user.is_authenticated:
        return HttpResponse(b'UNAUTHORIZED', status=401)
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(b'NOT FOUND', status=404)
    if product.user is None or product.user != request.user:
        return HttpResponse(b'FORBIDDEN', status=403)

    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price') or 0
    stock = request.POST.get('stock') or 0
    category = request.POST.get('category')
    thumbnail = request.POST.get('thumbnail')
    is_featured = request.POST.get('is_featured') in ['true','True','on','1','checked']

    if name is not None:
        product.name = name
    if description is not None:
        product.description = description
    try:
        product.price = int(price)
    except:
        product.price = 0
    try:
        product.stock = int(stock)
    except:
        product.stock = 0
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.save()
    return HttpResponse(b'UPDATED', status=200)


@require_POST
def delete_product_ajax(request, id):
    if not request.user.is_authenticated:
        return HttpResponse(b'UNAUTHORIZED', status=401)
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(b'NOT FOUND', status=404)
    if product.user is None or product.user != request.user:
        return HttpResponse(b'FORBIDDEN', status=403)
    product.delete()
    return HttpResponse(b'DELETED', status=200)