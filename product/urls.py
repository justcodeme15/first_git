from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('create/', views.create, name='product-create'),
    path('product/<int:id>', views.product_detail, name='product-detail'),
]