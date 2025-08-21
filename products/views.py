from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for pid, qty in cart.items():
        p = Product.objects.get(pk=int(pid))
        p.qty = qty
        p.subtotal = p.price * qty
        total += p.subtotal
        products.append(p)
    return render(request, 'cart.html', {'products': products, 'total': total})

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('product_list')
