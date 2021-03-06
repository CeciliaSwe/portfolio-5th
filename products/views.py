from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category

from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    categories = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        "products": products,
        "current_categories": categories,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """ Add a product to the store via the form """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can add products.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added!")
            return redirect(reverse("add_product"))
        else:
            messages.error(request, "Product not added, check form validity")
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can edit products.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f" {product.name} has been updated!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "Only store owners can delete products.")
        return redirect(reverse("home"))

    try:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, "Product deleted!")
        return redirect(reverse("products"))
    except:
        messages.error(request, "Deletion error!\
            Item has been purchased and cannot be removed")
        return redirect(reverse("products"))
