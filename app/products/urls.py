from django.urls import path

from .views import ProductsAPIView, ProductsTemplateView

urlpatterns = [
    path('api/products', ProductsAPIView.as_view(), name='products-api'),
    path('products/', ProductsTemplateView.as_view(), name='products')
]
