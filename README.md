# Car Sales By Dealers

Car Sales By Dealers is a Django-based web application and API framework designed for managing car sales, customer details, dealer information, and car inventory. This project provides CRUD (Create, Read, Update, Delete) operations for car sales, allowing dealers to manage their inventory and sales transactions.

## Features

- **User Authentication**: Secure user authentication and management system.
- **Car Management**: Add, edit, and delete car details, including make, model, year, and price.
- **Customer Management**: Record and manage customer information, including names, email addresses, and phone numbers.
- **Dealer Management**: Store and update dealer information, including names and locations.
- **Sales Transactions**: Create and manage sales transactions with details such as the car sold, the customer, and the dealer involved.
- **API Framework**: Provides API endpoints for interacting with the system programmatically.

## Getting Started

### Prerequisites

Before you start, ensure you have the following prerequisites:

- Python 3.8+
- Django 4.2+

### Installation

1. Clone the repository:

   ```bash
     git clone https://github.com/RAMANATHAN-19/CarSalesByDealersProject.git

## Deployment

To deploy this project run

1. Change your working directory:

```bash
  cd car-sales-by-dealers
```

2.Create a virtual environment (optional but recommended):
```bash
  python -m venv venv
  source venv/bin/activate
```
3.Apply database migrations:
```bash
  python manage.py makemigrations
  python manage.py migrate
```

4.Create a superuser account for the admin panel:
```bash
  python manage.py createsuperuser
```
5.Collect static files:
```bash
  python manage.py collectstatic
```
6.Start the development server:
```bash
  python manage.py runserver
```

You can now access the application at http://localhost:8000/ and the admin panel at http://localhost:8000/admin/. Log in with the superuser account you created.
## Usage

Access the admin panel by navigating to http://localhost:8000/admin/ and log in with the superuser account.

To access the user interface, visit http://localhost:8000/.

Configuration
You can configure various settings for this project by modifying the settings.py file. Some of the settings you can customize include:

Database settings: Configure your database connection and settings.

Static and media file settings: Adjust the paths and locations for static and media files.

And more: Explore other settings in the settings.py file to tailor the project to your specific requirements.
## Running Tests

To run tests, run the following command

TO RUN THE DJANGO ADMIN
```
http://127.0.0.1:8000/admin/
```

  TO RUN THE API
```
http://127.0.0.1:8000/api/
```
## API Endpoints:

### Car API

- **Endpoint:** `/api/cars/`
- **Description:** Get a list of cars and create new car entries.
- **Methods:** GET, POST, PUT, DELETE

### Customer API

- **Endpoint:** `/api/customer/`
- **Description:** Manage customer details.
- **Methods:** GET, POST, PUT, DELETE

### Dealer API

- **Endpoint:** `/api/dealers/`
- **Description:** Get a list of dealers information..
- **Methods:** GET, POST, PUT, DELETE

### Sales API

- **Endpoint:** `/api/sales/`
- **Description:** View, create, and manage sales transactions.
- **Methods:** GET, POST, PUT, DELETE


