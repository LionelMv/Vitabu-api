# Vitabu
This API provides a simple service for managing customers and their orders, implementing secure authentication using OpenID Connect (OIDC) and sending SMS notifications upon order creation. The application is built using Django and Django REST Framework (DRF) with PostgreSQL as the database, and leverages Africa’s Talking SMS gateway for real-time alerts.

## Key Features
1. **Customer Management:** Create, update, and view customers, including details such as name, email, and unique codes.

2. **Order Management:** Create and view orders linked to customers, with details such as item name, amount, and order timestamp.

3. **Authentication and Authorization:** Secure access to the API using OpenID Connect (OIDC) via django-allauth, enabling seamless integration with identity providers like Google for OAuth2-based authentication.

4. **SMS Notifications:** Upon successful order creation, the API sends an SMS notification to the customer's registered phone number using Africa’s Talking SMS gateway.
5. **Testing and CI/CD:** Includes comprehensive unit tests to ensure reliability, with continuous integration and deployment setups for automated testing and deployment.

## Technologies Used
- **Backend:** Python, Django, Django REST Framework
Database: PostgreSQL
- **Authentication:** OpenID Connect (OIDC) via django-allauth
- **SMS Alerts:** Africa’s Talking SMS gateway
- **CI/CD:** GitHub Actions

## Setup & Installation
1. Clone the repository.
2. Install pipenv:
    - On Linux
        ```sh
        sudo apt-get install pipenv
        ```
    - On macOS or Windows
        ```sh
        pip install pipenv
        ```
3. Setup project environment:
    ```sh
    pipenv install
    ```
4. Activate the project environment:
    ```sh
    pipenv shell
    ```
    For more information about Pipenv, check: [Pipenv: A Guide to The New Python Packaging Tool - Real Pyhton](https://realpython.com/pipenv-guide/)

5. Copy the envsample file to the root folder with the name ```.env```.
    Change settings and configurations on the ```.env``` file:
    - Database settings: Used PostgreSQL for this project.
    - All Auth settings: Google's client_id and client_secret.
    - Africa's Talking Settings: username and api key

6. Make changes to your database:
    ```sh
    python manage.py migrate
    ```
7. Usage:
    ```sh
    cd Vitabu-api
    python manage.py runserver
    ```
    On your browser, run the following link: http://localhost:8000/accounts/login.
    Tap on Google to sign in with Google to access the API.

## API Documentation
The documentation of the API created using Django Rest Framework (DRF) is on the file ```api.md```.

## Contributing
Want to make TradersIn better?
- Fork the project.
- Create a new branch to work on ```git checkout -b <feature_branch>```
- You can name the branch with the prefix ```feature_```
- Add your changes and push them to the branch: ```git push```
- Open a pull request


## Authors
Lionel Gicheru [LinkedIn](https://www.linkedin.com/in/lionelmwangi/)
