from django.shortcuts import render
from .models import Products,Categoty,Promotion
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ProductSerializer
from .serializers import CategotySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    
class CategotyViewSet(ModelViewSet):
    queryset = Categoty.objects.all()
    serializer_class = CategotySerializer
    permission_classes = [IsAuthenticated]
    
    # permission_classes = [IsAuthenticatedOrReadOnly]

# Example of fetching data
# def fetch_data():

#     queryset = Products.objects.all()

#     for obj in queryset:
       
#         print(obj.title)
#         print(obj.price)  


# fetch_data()

# def fetch_data_with_select_related():
#     # using select_related products to catagory 
#     queryset = Products.objects.select_related('category').all()

#     # Print each product and its related category title
#     for product in queryset:
#         print(f"Product: {product.title}")
#         print(f"Product: {product.description}")
#         print(f"Product: {product.price}")
#         print(f"Product: {product.last_update}")
#         print(f"Product: {product.inventory}")
#         if product.category:
#             print(f"Category: {product.category.title}")
#         else:
#             print("Category: None")
#         print("")  
        
        
# def fetch_data_with_prefetch_related():
#     # Using prefetch_related products to promotion
#     queryset = Products.objects.prefetch_related('promotion').all()

#     # Print each product and its related promotions
#     for product in queryset:
#         print(f"Product: {product.title}")
#         print(f"Product: {product.description}")
#         print(f"Product: {product.price}")
#         print(f"Product: {product.last_update}")
#         print(f"Product: {product.inventory}")
#         print("Promotions:")
#         for promotion in product.promotion.all():
#             print(f"- {promotion.description}, {promotion.discount}% off")
        # print("")  
        
class CategotyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        snippets = Categoty.objects.all()
        serializer = CategotySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategotySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class CategotyDetails(APIView):
      
    def get_object(self, pk):
        try:
            return Categoty.objects.get(pk=pk)
        except Categoty.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategotySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategotySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    