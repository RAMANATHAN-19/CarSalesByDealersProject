from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Dealer, Customer, Sale
from .serializers import CarSerializer, DealerSerializer, CustomerSerializer, SaleSerializer
from django.views.generic import TemplateView
from django.http import Http404

class HomeView(TemplateView):
    template_name = 'home.html'
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # GET action
    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    # POST action
    def create(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE action
    def destroy(self, request, *args, **kwargs):
        try:
            car = self.get_object()
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
    # PUT(update) action
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CarSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    # GET action
    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # Implement your logic here
        dealers = Dealer.objects.all()
        serializer = DealerSerializer(dealers, many=True)
        return Response(serializer.data)

    # POST action
    def create(self, request, *args, **kwargs):
        serializer = DealerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE action
    def destroy(self, request, *args, **kwargs):
        try:
            dealer = self.get_object()
            dealer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    # PUT(update) action
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DealerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # GET action
    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # Implement your logic here
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    # POST action
    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE action
    @action(detail=True, methods=['delete'])
    def delete_customer(self, request, pk=None):
        try:
            customer = self.get_object()
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # PUT(update) action
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    # GET action
    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        # Implement your logic here
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    # POST action
    def create(self, request, *args, **kwargs):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE action
    def destroy(self, request, *args, **kwargs):
        try:
            sale = self.get_object()
            sale.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    # PUT(update) action
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SaleSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
