from django.shortcuts import render, get_object_or_404
from .cart import Cart
from home.models import Product
from django.http import JsonResponse

# Create your views here.

# Defining cart summary
def cart_summary(request):
    #get the cart...
    cart=Cart(request)
    cart_products=cart.get_prods()
    return render(request, 'cart_summary.html', {"cart_products": cart_products})

# Adding the cart add
def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST request
    if request.POST.get('action') == 'post':
        # Get product ID
        product_id = int(request.POST.get('product_id'))
        # Look up product in the database
        product = get_object_or_404(Product, id=product_id)  # Changed 'product' to 'Product'
        # Save to session
        cart.add(product=product)

        # Get Cart Quantity
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty':cart_quantity})
        return response

        # Return response
        response = JsonResponse({'Product Name': product.name})  # Fixed syntax
        return response
