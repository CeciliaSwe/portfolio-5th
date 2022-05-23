from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
        messages.success(request, f"Quantity of {product.name} updated")

    else:
        cart[item_id] = quantity
        messages.success(request, f"{product.name} added to your cart")

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f"Updated quantity of {product.name}")

    else:
        cart.pop(item_id)
        messages.success(request, f"Removed {product.name} from your cart")

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = Product.objects.get(pk=item_id)
        cart = request.session.get("cart", {})
        cart.pop(item_id)
        messages.success(request, f" {product.name} was removed from your bag")

        request.session["cart"] = cart
        return redirect(reverse("view_cart"))

    except Exception as e:
        return HttpResponse(status=500)
