from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from KeyLuxury.models import App, Device_costumer, Producto_sale
from KeyLuxury.forms import ProductsForm, RegisterUser


def Form_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()  
            success_url = reverse("Welcome")
            return redirect(success_url)
    else:  # GET
        form = RegisterUser()
    return render(
        request=request,
        template_name='KeyLuxury/User.html',
        context={'form': form},
    ) 

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='KeyLuxury/LogIn.html',
        context={'form': form},
    )


def Welcome(request):
    return render(request=request, template_name= 'KeyLuxury/Welcome.html')

def Categories(request):
    return render(request=request, template_name= 'KeyLuxury/Categories.html')

def Products(request): 
    contexto = Producto_sale.objects.all()
    return render(
        request=request,
        template_name='KeyLuxury/Products.html',
        context={'form': contexto},
    )

def Create_Products(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Product = Product(name=data['name'], Price=data['Price'], Description=data['Descritcion'])
            Product.save()
            url_exitosa = reverse('Products')
            return redirect(url_exitosa)
    else:   #GET
        form = ProductsForm()
    return render(
        request=request,
        template_name='KeyLuxury/Create_Products.html',
        context={'form': form},
    )

def See_Products(request, id):
    Product = Producto_sale.objects.get(id=id)
    contexto = {
        'Product': Product
    }
    return render(
        request=request,
        template_name='Keyluxury/See_Products.html',
        context=contexto,
    )

def Edit_Product (request, id): 
    Product = Producto_sale.objects.get(id=id)
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Product.name= data['name']
            Product.price = data['price'] 
            Product.description = data['description']
            Product.save()
            url_exitosa = reverse('Products')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'name': Product.name_product,
            #'Price': Producto_sale.Price,
            #'Description': Product.Description,
        }
        form = ProductsForm(initial=inicial)
    return render(
        request=request,
        template_name='KeyLuxury/Edit_Products.html',
        context={'form': form},
    )

def Delete_Product (request, id):
    Product = Producto_sale.objects.get(id=id)
    if request.method == "POST":
        Product.delete()
        url_exitosa = reverse('Products')
        return redirect(Products)
    
def About (request):
    return render(request=request, template_name= 'KeyLuxury/About.html')

def BlogReview (request):
    return render(request = request, template_name= 'KeyLuxury/BlogReview.html')

def LogIn (request):
    return render(request = request, template_name= 'KeyLuxury/LogIn.html')