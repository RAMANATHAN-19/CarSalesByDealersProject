"""car_dealer_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from car_dealer.views import HomeView, CarViewSet, DealerViewSet, CustomerViewSet, SaleViewSet
from django.contrib.staticfiles import views

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'dealers', DealerViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('cars/<int:pk>/', CarViewSet.as_view({'get': 'retrieve'}), name='car-detail'),
    path('dealers/<int:pk>/', DealerViewSet.as_view({'get': 'retrieve'}), name='dealer-detail'),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve'}), name='customer-detail'),
    path('sales/<int:pk>/', SaleViewSet.as_view({'get': 'retrieve'}), name='sale-detail'),
    path('api/', include(router.urls)),
    path("static/<path:path>", views.serve),
]



