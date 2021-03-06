import arrow
from django.shortcuts import render
from .models import Product, Purchase


def all_products(request):
    """
    Show products page.
    Render products.html template with a list of all the
    products saved on the Product Model.
    Use Purchase model to show the user its active products,
    highlighting the ones expiring soon
    """

    products = Product.objects.all().order_by('-name')
    # passed as argument to compare the products with an active licence
    # in the template
    today = arrow.now()
    # passed as argument to highlight the products close to expire
    expire_soon = arrow.now().replace(days=+30).datetime
    purchases = Purchase.objects.filter(user_id=request.user.id)\
        .order_by('license_end')
    args = {'products': products, 'purchases': purchases, 'today': today,
            'expire_soon': expire_soon}
    for product in products:
        print product.image.name
    return render(request, "products/products.html", args)
