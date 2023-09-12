from django.contrib import admin
from django.urls import path, include
from products.views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', basket_delete, name='basket_delete'),
]
