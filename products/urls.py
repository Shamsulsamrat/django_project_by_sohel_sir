from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductViewSet
from .views import Categoty
from products import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'categoty', Categoty)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('categoty/', views.CategotyView.as_view()),
    path('categoty/<int:pk>/', views.CategotyDetails.as_view()),   
]



