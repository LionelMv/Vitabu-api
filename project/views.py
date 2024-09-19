from rest_framework import generics
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Order Views
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # Overriding the create method to associate the order with a customer
    def perform_create(self, serializer):
        customer_id = self.request.data.get('customer_id')
        customer = Customer.objects.get(id=customer_id)
        serializer.save(customer=customer)


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
