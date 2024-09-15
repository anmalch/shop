# Shop Management System

This is a Django-based web application designed for managing products in an online store. The system provides features for product management, and serves both static and dynamic content through Django's templating system.

## Features

- Product management (CRUD operations: Create, Read, Update, Delete)
- Django Admin for easy management of products
- Database-backed application (SQLite by default)
- Structured with reusable components for scalability
- Static file serving through Django

## Project Structure

```
shop-main/
├── .gitignore
├── README.md              # Project documentation
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── products/              # App responsible for handling product-related operations
│   ├── admin.py           # Django admin customization for products
│   ├── apps.py            # App configuration
│   ├── models.py          # Database models for products
│   ├── views.py           # Views for product-related operations
│   ├── templates/         # HTML templates for rendering product pages
│   ├── migrations/        # Database migrations
│   └── tests.py           # Unit tests for the product app
├── shop/                  # Main project folder with settings and URLs
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing for the project
│   ├── wsgi.py            # WSGI configuration for deployment
│   └── asgi.py            # ASGI configuration for asynchronous support
├── static/                # Static files (CSS, JavaScript, images)
```

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/shop-main.git
   cd shop-main
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

- Use the Django admin panel to manage products, categories, and other related entities.
- Access the product pages through the main app routes.
