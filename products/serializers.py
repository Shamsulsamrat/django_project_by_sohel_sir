from rest_framework import serializers
from .models import Products
from .models import Categoty
from .models import Promotion

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__' 
        
class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoty
        fields = '__all__' 