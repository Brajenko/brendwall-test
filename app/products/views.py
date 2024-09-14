from rest_framework.generics import ListCreateAPIView
from django.views.generic import TemplateView

from .serializers import ProductSerializer
from .models import Product

class ProductsAPIView(ListCreateAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsTemplateView(TemplateView):
    template_name = 'index.html'
