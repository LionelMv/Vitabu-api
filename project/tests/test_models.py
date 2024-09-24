from django.test import TestCase
from ..models import Customer, Order
from django.utils import timezone
from unittest.mock import patch
from unittest import mock


class CustomerModelTest(TestCase):

    def setUp(self):
        # Create a customer object for testing
        self.customer = Customer.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            code='CUST123'
        )

    def test_customer_creation(self):
        """Test that a customer object is created successfully"""
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.email, 'johndoe@example.com')
        self.assertEqual(self.customer.code, 'CUST123')

    def test_customer_str_method(self):
        """Test the __str__ method of the Customer model"""
        self.assertEqual(str(self.customer), 'John Doe (CUST123)')


class OrderModelTest(TestCase):

    @patch('project.signals.send_sms_alert')
    def setUp(self, mock_send_sms):
        # Create a customer object
        self.customer = Customer.objects.create(
            name='Jane Doe',
            email='janedoe@example.com',
            code='CUST456',
            phone_number='+254705'
        )

        mock_send_sms.return_value = None

        # Create an order object
        self.order = Order.objects.create(
            item='Book A',
            amount=20.00,
            customer=self.customer,
            time=timezone.now()
        )
        mock_send_sms.assert_called_once_with(self.customer.phone_number, mock.ANY)

    def test_order_creation(self):
        """Test that an order object is created successfully"""
        self.assertEqual(self.order.item, 'Book A')
        self.assertEqual(self.order.amount, 20.00)
        self.assertEqual(self.order.customer, self.customer)

    def test_order_str_method(self):
        """Test the __str__ method of the Order model"""
        expected_str = (
            f"Order of Book A for 20.00 by {self.customer.name} "
            f"at {self.order.time}"
        )
        self.assertEqual(str(self.order), expected_str)
