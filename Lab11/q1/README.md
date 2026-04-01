# Book Management System

A Django-based web application for managing books, authors, and publishers.

## Project Structure

```
bookproject/          # Django project settings
bookapp/              # Main application
├── models.py         # Database models (Author, Publisher, Book)
├── forms.py          # Django forms for data input
├── views.py          # View functions
├── urls.py           # URL routing
├── admin.py          # Django admin configuration
├── templates/        # HTML templates
└── static/
    └── css/
        └── style.css # Minimal styling
```

## Models

### Author
- first_name (CharField)
- last_name (CharField)
- email (EmailField)

### Publisher
- name (CharField)
- street_address (CharField)
- city (CharField)
- state_province (CharField)
- country (CharField)
- website (URLField)

### Book
- title (CharField)
- publication_date (DateField)
- authors (ManyToManyField to Author)
- publisher (ForeignKey to Publisher)

## Installation and Setup

1. Make sure Django is installed:
   ```bash
   pip3 install django
   ```

2. Navigate to the project directory:
   ```bash
   cd Lab11/q1
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

## Features

### CRUD Operations
- **Authors**: Create, read, update, delete authors
- **Publishers**: Manage publisher information
- **Books**: Create books with multiple authors and a publisher

### Pages

1. **Home Page** - Dashboard with quick stats
2. **Authors** - List all authors with CRUD operations
3. **Publishers** - Manage publishers
4. **Books** - Create and manage books with many-to-many author relationships

### Forms

All forms are defined in `forms.py` using Django's ModelForm:
- `AuthorForm` - For author creation/editing
- `PublisherForm` - For publisher management
- `BookForm` - For book management with multiple author selection using checkboxes

## Navigation

Main menu items:
- Home
- Authors
- Publishers
- Books

Each page has buttons to:
- Create new entries
- View details
- Edit existing entries
- Delete entries (with confirmation)

## Minimal CSS Design

The site uses a basic, clean design with:
- Navigation bar
- Table layouts for lists
- Simple form styling
- Button styles for actions
- Responsive mobile design
- Minimal color scheme (blue/gray)

## Running the Server

To start the server:
```bash
python3 manage.py runserver
```

The server will be available at: http://127.0.0.1:8000/

## Admin Access

To access the Django admin panel:
1. Create a superuser: `python3 manage.py createsuperuser`
2. Go to: http://127.0.0.1:8000/admin/
3. Login with your superuser credentials

## Notes

- Database: SQLite (db.sqlite3)
- All HTML templates are in `bookapp/templates/`
- CSS is minimal and located at `bookapp/static/css/style.css`
- The application uses Django's built-in form handling and validation
