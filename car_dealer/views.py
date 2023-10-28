from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Dealer, Customer, Sale
from .serializers import CarSerializer, DealerSerializer, CustomerSerializer, SaleSerializer
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        return Response(...)

class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        return Response(...)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        return Response(...)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        return Response(...)
