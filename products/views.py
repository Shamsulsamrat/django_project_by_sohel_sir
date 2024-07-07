from django.shortcuts import render
from .models import Products,Categoty,Promotion
from django.db.models import Count


# Create your views here.

def test_view(request):
    # query_set = Products.objects.all()
    #Filter
    
    # query_set = Products.objects.filter(title__startswith ="B",price__lte=1300) 
    
    # query_set = Products.objects.filter(category__id=1) 
    
    # query_set = Products.objects.filter(promotion__discount=15) 
    
    
    # query_set = Categoty.objects.filter(products__title="Bike") 
    
    # query_set = Promotion.objects.filter(Products__discount=15) 
    
    #GET 
    # product = Products.objects.get(id=100) 
    # product = Products.objects.filter(id=2).first()
    
    # query_set = Products.objects.get(promotion__discount=15)
    
    q = Products.objects.annotate(product_id= Count("id"))
    print(q[0].product_id)
    
    # print(query_set[])
    # for item in query_set:
    #     print(item.title)
    # print(product)
        # print(item.price)
    # return render(request, 'hello.html', {"data":query_set})
    
    
    return render(request, 'hello.html', {"data":{}})

