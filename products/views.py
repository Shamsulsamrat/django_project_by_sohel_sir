from django.shortcuts import render
from .models import Products,Categoty,Promotion
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

