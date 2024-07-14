# Django Dish Search Application

This is a Django application that allows users to search for dish names and recommend the best match from a dataset.

## Project Setup

### Prerequisites

- Python 3.6 or higher
- Django 4.x
- Requests library (for fetching data from a URL)

### Installation

Create a virtual environment:
  
    python -m venv venv

Activate the virtual environment:
    
    venv\Scripts\activate

Install the required dependencies:
    
    pip install -r requirements.txt

Running the Application

Apply migrations:
    
    python manage.py makemigrations
    python manage.py migrate

Create a superuser (for accessing the admin interface):
    
    python manage.py createsuperuser

Load the initial data from the CSV file:
    
    python manage.py load_dishes

Run the development server:
    
    python manage.py runserver

Access the application:

Admin Interface: http://127.0.0.1:8000/admin
Search Interface: http://127.0.0.1:8000/search/


Project Structure
  dish_search/: Root directory of the project.
    search/: Django app containing the search functionality.
      models.py: Defines the Dish model.
      views.py: Contains the search view.
      admin.py: Registers the model with the admin interface.
      management/commands/load_dishes.py: Custom management command to load data from CSV.
    dish_search/: Project settings directory.
      settings.py: Project settings.
      urls.py: URL configurations.
      manage.py: Django management script.
      
