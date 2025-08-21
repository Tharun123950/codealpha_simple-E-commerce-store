Simple Django e-commerce sample (minimal)

How to run locally (Windows Command Prompt):
1. Install Python 3.10+ from https://www.python.org/downloads/
2. Open Command Prompt and navigate to the project folder (where manage.py is)
   e.g. cd C:\path\to\myshop_project
3. (Optional but recommended) create & activate a virtualenv:
   python -m venv venv
   venv\Scripts\activate
4. Install Django:
   pip install django
5. Run migrations and create superuser:
   python manage.py migrate
   python manage.py createsuperuser
6. Run the dev server:
   python manage.py runserver 8000
7. Open http://127.0.0.1:8000/ to view the product list, and http://127.0.0.1:8000/admin/ to add products.

Note: This is a minimal example for learning. Do not use DEBUG=True in production.
