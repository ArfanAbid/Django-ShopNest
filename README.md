# ShopNest 

ShopNest is an online marketplace developed using Django, Tailwind CSS, and MySQL database. 

- ShopNest is a  web application that provides a platform for users to buy and sell various products. The project is built using Django, a high-level web framework for  Python, Tailwind CSS for styling, and MySQL as the database.



## Features

- User authentication and authorization
- Product listing and details
- User profiles
- Admin panel for managing products and orders

## Installation

- Python [Install Python](https://www.python.org/downloads/)
- Django (install using pip): `pip install django`

1. Clone the repository:

   ```bash
   git clone https://github.com/ArfanAbid/Django-ShopNest.git

2. Navigate to project directory:
    `cd core`
   
3. Create and activate Virtual Environment:
   `python -m venv venv` then
   `.\venv\Scripts\activate`
4. Set up MySQL:

   - Create a MySQL database named "my_database".
   - Update the database configuration in settings.py with your MySQL credentials:

```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',   # Name database according to your choice
        'USER': 'root',
        'PASSWORD': ' ', #you set while Settingup MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

5. Run Data base migrations:
   `python manage.py migrate`

6. Create a superuser (admin account) to access the Django admin panel:
   `python manage.py createsuperuser`

7. Run the development server:
   `python manage.py runserver`

8. Access the development server at  `http://127.0.0.1:8000/`

## Contributing:

Contributions are welcome! Fork the repository, make your changes, and submit a pull request explaining the improvements or additions you've made.🤝