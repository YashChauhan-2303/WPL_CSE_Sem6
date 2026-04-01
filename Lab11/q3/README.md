# Human Management System

A Django-based web application for managing human records with dropdown selection, text input, and update/delete functionality.

## Features

✅ **Dropdown List** - Displays all first names from the Human table
✅ **Add New Person Form** - Add new records directly from the main page
✅ **Text Boxes** - Shows and allows editing of first name, last name, phone, address, and city
✅ **Update Button** - Updates the selected record in the database
✅ **Delete Button** - Deletes the selected record and refreshes the dropdown
✅ **Auto-refresh** - Dropdown automatically re-populates after delete operation
✅ **Confirmation** - Delete action requires user confirmation
✅ **Sample Data** - Load 5 sample records with: `python3 manage.py load_sample_data`

## Database Model

**Human Table:**
- first_name (CharField)
- last_name (CharField)
- phone (CharField)
- address (CharField)
- city (CharField)

## Installation and Setup

1. Make sure Django is installed:
   ```bash
   pip3 install django
   ```

2. Navigate to the project directory:
   ```bash
   cd Lab11/q3
   ```

3. Apply migrations (already done):
   ```bash
   python3 manage.py migrate
   ```

4. Create a superuser (optional, for admin access):
   ```bash
   python3 manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

6. Open your browser and go to:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## How to Use

1. **Load the page** - You'll see a dropdown list with all first names
2. **Select a name** - Choose a person from the dropdown list
3. **View details** - Their information appears in the text boxes
4. **Edit details** - Modify any field (first name, last name, phone, address, city)
5. **Update** - Click the Update button to save changes
6. **Delete** - Click the Delete button to remove the record. A confirmation dialog will appear.
7. **Refresh** - After deleting, the dropdown list automatically refreshes

## Project Structure

```
humanproject/
├── __init__.py
├── settings.py
├── urls.py
├── wsgi.py
└── asgi.py

humanapp/
├── models.py (Human model with fields)
├── forms.py (HumanForm for data)
├── views.py (CRUD operations with dropdown)
├── urls.py (URL routing)
├── admin.py (Admin customization)
├── apps.py
├── migrations/
│   └── 0001_initial.py
└── templates/
    └── index.html (Main page with dropdown)

manage.py
db.sqlite3 (Database)
```

## Adding Sample Data

To add sample data, use the admin panel:

1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Click on "Humans" and add records
4. Return to the main page and select from the dropdown

## Frontend

- **Basic HTML** - No CSS styling, pure HTML form elements
- **Dropdown (Select)** - Auto-submits form on selection
- **Text Inputs** - For editing individual fields
- **Buttons** - Update and Delete actions
- **Confirmation Dialog** - For delete operation safety

## Technology Stack

- Backend: Django 5.2
- Database: SQLite
- Frontend: Basic HTML with form elements
- No CSS - Minimal styling
