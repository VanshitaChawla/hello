
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from home.models import CartItem, Contact, Order, Product
from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def ecom(request):
    if request.user.is_anonymous:
        return redirect("/login")

    trending_products = Product.objects.filter(rating__gt=3)
    one_week_ago = timezone.now() - timedelta(days=7)
    new_products = Product.objects.filter(pub_date__gte=one_week_ago)
    
    context = {
        'trending_products': trending_products,
        'new_products': new_products,
        'active_page': 'ecom'
    }
    
    return render(request, 'ecom.html', context)

def about(request):
    context = {'active_page': 'about'}
    return render(request, 'about.html', context)

def blog(request):
    context = {'active_page': 'blog'}
    return render(request, 'blog.html', context)

def cart(request):
    if request.user.is_anonymous:
        return redirect("/login")

    cart_items = CartItem.objects.filter(user=request.user)  
    total = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
        'active_page': 'cart'
    }
    return render(request, 'cart.html', context)

def product(request, id):
    if request.user.is_anonymous:
        return redirect("/login")

    try:
        product_fetch = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Product not found.", status=404)

    featured_products = Product.objects.filter(rating__gte=3)
    context = {
        'product': product_fetch,
        'featured_products': featured_products,
        'active_page': 'product'
    }
    return render(request, 'product.html', context)

def shop(request):
    products = Product.objects.all()
    context = {'products': products, 'active_page': 'shop'}
    return render(request, 'shop.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phoneno=phoneno, desc=desc)
        contact.save()
        messages.success(request, 'Contact created')
    context = {'active_page': 'contact'}
    return render(request, 'contact.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

@csrf_exempt
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        size = request.POST.get('size', 'S')

        cart_item, created = CartItem.objects.get_or_create(
            product=product,
            user=request.user,
            size=size,
            defaults={'quantity': quantity},
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        messages.success(request, 'Item added to cart successfully!')
        return redirect('cart')

    return HttpResponse("Invalid request method.", status=400)


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart successfully!')
    return redirect('cart')

def Check_out_cart(request,total):
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method=='POST':
        address_line_1 = request.POST.get('address_line_1')
        name=request.POST.get('name')
        email=request.POST.get('email')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        
        Order.objects.create(
            user=request.user,
            address_line_1=address_line_1,
            name=name,
            email=email,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            totsl=total
        )
        CartItem.objects.filter(user=request.user).delete()
        
        messages.success(request, 'Order placed successfully!')
        return redirect('/')
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'active_page': 'checkout'
    }
    
    return render(request, 'checkout.html', context)
    
