from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView

from products.models import Product, ProductCategory, Basket

from users.models import User


class IndexView(TemplateView):
    template_name = "products/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Store'
        return context


# def index(request):
#     context = {
#         'title': 'Store',
#     }
#     return render(request, 'products/index.html', context)
#

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    items = Basket.objects.filter(user=request.user, product=product)

    if not items.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        item = Basket.objects.get(user=request.user, product=product)
        item.quantity += 1
        item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
