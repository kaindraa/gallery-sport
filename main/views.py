from django.shortcuts import render, redirect, reverse   # Tambahkan import redirect di baris ini
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    # products = Product.objects.all()
    # products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'price': 150000,
        'description': 'Jersey Timnas, Ukuran XL, Original',
        'quantity': 10,
        'discount': 0.0,
        # 'products': products,
        'last_login': request.COOKIES.get('last_login', 'Empty')


    }
    

    return render(request, "main.html", context)


def create_product_entry(request):
    print(1)
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        print(2)

        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    else:
        print(3)  

    context = {'form': form}
    return render(request, "create_product_entry.html", context)


def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form valid")
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            print("Form ga valid")
            print(form.errors)  # Debugging: print form errors to the console
    
    context = {'form': form}
    return render(request, 'register.html', context)



def login_user(request):
    if request.method == 'POST':
        print("Form submission received:", request.POST)  # Print form data
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            print("Form is valid")
            user = form.get_user()
            print("Authenticated user:", user)
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            print("Form is invalid")
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request,id):
    product = Product.objects.get(pk=id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form':form}
    return render(request, "edit_product.html", context)
    
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    quantity = request.POST.get("quantity")
    discount = request.POST.get("discount")
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        quantity=quantity,
        discount=discount,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)


from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            new_product = Product.objects.create(
                user=request.user,  # Assuming the user is logged in
                name=data["name"],
                price=int(data["price"]),
                description=data["description"],
                quantity=int(data["quantity"]),
                discount=float(data["discount"])
            )

            new_product.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


@csrf_exempt
def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(user=request.user)
        data = [
            {
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "quantity": product.quantity,
                "discount": product.discount,
            }
            for product in products
        ]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)
