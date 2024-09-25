# API Documentation
### Customer Endpoints
1. List All Customers
- URL: /api/customers
- Method: GET
- Description: Retrieve a list of all customers.
- Response Example:
    ```sh
    [
        {
            "id": 2,
            "name": "Mwangi",
            "email": "mvangicode@gmail.com",
            "code": "CUST254",
            "phone_number": "+25470...."
        },
        ...
    ]
    ```

2. Retrieve, Update, or Delete a Specific Customer

- URL: api/customers/\<int:pk\>/
- Methods: GET, PUT, DELETE
- Description: Retrieve, update, or delete a specific customer by their primary key.
- Response Example (GET):
    ```sh
    {
        "id": 2,
        "name": "Mwangi",
        "email": "mvangicode@gmail.com",
        "code": "CUST254",
        "phone_number": "+25470...."
    }
    ```

### Order Endpoints
3. List All Orders
- URL: /orders/
- Method: GET
- Description: Retrieve a list of all orders.
- Response Example:
    ```sh
    [
        {
            "id": 2,
            "item": "Book A",
            "amount": "20.00",
            "time": "2024-09-24T21:21:28.341126Z",
            "customer": {
                "id": 2,
                "name": "Mwangi",
                "email": "mvangicode@gmail.com",
                "code": "CUST254",
                "phone_number": "+25470..."
            }
        },
        ...
    ]
    ```

4. Retrieve, Update, or Delete a Specific Order

- URL: /orders/\<int:pk\>/
- Methods: GET, PUT, PATCH, DELETE
- Description: Retrieve, update, or delete a specific order by their primary key.
- Response Example (GET):
    ```sh
    {
        "id": 2,
        "item": "Book A",
        "amount": "20.00",
        "time": "2024-09-24T21:21:28.341126Z",
        "customer": {
            "id": 2,
            "name": "Mwangi",
            "email": "mvangicode@gmail.com",
            "code": "CUST254",
            "phone_number": "+254705305054"
        }
    }
    ```
