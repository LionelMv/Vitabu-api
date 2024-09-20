from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer, Order


class VitabuAPITestCase(APITestCase):
    def setUp(self):
        """Setup to create sample data"""
        # Create a sample customer for testing
        self.customer = Customer.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            code="CUST123"
            )

        # Create a sample order for testing
        self.order = Order.objects.create(
            customer=self.customer,
            item="Book B",
            amount=20.00,
        )

        # Prepare URLs for customer and order APIs
        self.customer_url = reverse('customer-list')
        self.order_url = reverse('order-list')

        # Sample data for POST requests
        self.valid_customer_data = {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "code": "CUST456"
            }
        self.valid_order_data = {
            "customer_id": self.customer.id,
            "item": "Book A",
            "amount": 10.99,
            "time": "2024-09-19T10:00:00Z"
        }

    def test_create_customer(self):
        """Test to create a new customer"""
        # Send a POST request to create a customer
        response = self.client.post(
            self.customer_url,
            self.valid_customer_data,
            format='json'
            )
        # print("Response Data:", response.data)  # for debugging

        # Check if the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the customer was created in the database
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.last().name, "Jane Doe")

    def test_get_customers(self):
        """Test to get all customers"""
        # Send a GET request to retrieve customers
        response = self.client.get(self.customer_url)

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the sample customer
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John Doe")
        self.assertEqual(response.data[0]['code'], "CUST123")
        self.assertEqual(response.data[0]['email'], "johndoe@example.com")

    def test_create_order(self):
        """Test to create a new order"""
        # Send a POST request to create an order
        response = self.client.post(
            self.order_url,
            self.valid_order_data,
            format='json'
            )
        # print("Response Data:", response.data)  # for debugging

        # Check if the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the order was created in the database
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(Order.objects.last().item, "Book A")

    def test_get_orders(self):
        """Test to get all orders"""
        # Send a GET request to retrieve orders
        response = self.client.get(self.order_url)

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the sample order
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['item'], "Book B")

    def test_retrieve_customer(self):
        """Test retrieving a single customer"""
        # Send a GET request to retrieve the customer
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.get(url)

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the response data
        self.assertEqual(response.data['name'], self.customer.name)
        self.assertEqual(response.data['email'], self.customer.email)

    def test_update_customer(self):
        """Test updating a customer"""
        # Send a PUT request to update the customer
        updated_data = {
            "name": "John Updated",
            "email": "johnupdated@example.com",
            "code": "CUST123UPDATED"
        }
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.put(url, updated_data, format='json')

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the customer data was updated in the database
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, updated_data['name'])
        self.assertEqual(self.customer.email, updated_data['email'])

    def test_delete_customer(self):
        """Test deleting a customer"""
        # Send a DELETE request to delete the customer
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.delete(url)

        # Check if the response status is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the customer was removed from the database
        self.assertEqual(Customer.objects.count(), 0)

    def test_retrieve_order(self):
        """Test retrieving a single order"""
        # Send a GET request to retrieve the order
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url)

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the response data
        self.assertEqual(response.data['item'], self.order.item)
        self.assertEqual(response.data['amount'],
                         format(self.order.amount, '.2f'))
        self.assertEqual(response.data['customer']['name'], self.customer.name)

    def test_update_order(self):
        """Test updating an order"""
        # Send a PUT request to update the order
        updated_order_data = {
            "customer_id": self.customer.id,
            "item": "Updated Book C",
            "amount": 35.00,
            "time": "2024-09-20T10:00:00Z"
        }
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.put(url, updated_order_data, format='json')

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the order data was updated in the database
        self.order.refresh_from_db()
        self.assertEqual(self.order.item, updated_order_data['item'])
        self.assertEqual(self.order.amount, updated_order_data['amount'])

    def test_delete_order(self):
        """Test deleting an order"""
        # Send a DELETE request to delete the order
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)

        # Check if the response status is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the order was removed from the database
        self.assertEqual(Order.objects.count(), 0)

    def test_list_orders_for_customer(self):
        """Test listing all orders for a customer"""
        # Create a couple of orders
        Order.objects.create(
            customer=self.customer,
            item="Book E",
            amount=50.00
            )
        Order.objects.create(
            customer=self.customer,
            item="Book F",
            amount=60.00
            )

        # Send a GET request to list orders for the customer
        url = reverse('order-list') + f'?customer={self.customer.id}'
        response = self.client.get(url)
        # print("Response data: ", response.data) # for debugging

        # Check if the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the response contains two orders
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[1]['item'], "Book E")
        self.assertEqual(response.data[2]['item'], "Book F")
