# Web Directory - Django Application

A professional web directory application built with Django. Manage website links organized by categories with tracking for visits and likes.

## Features

- **Category Management**: Create, read, update, and delete website categories
- **Page/Link Management**: Add and manage website links within categories
- **Statistics Tracking**: Track visits and likes for categories and views for pages
- **Professional UI**: Clean, responsive design with no unnecessary styling
- **Forms**: Custom Django forms for data entry
- **Admin Interface**: Full Django admin panel for management
- **Pagination**: Browse large datasets efficiently

## Project Structure

```
directory_project/
├── directory_project/          # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI application
│   └── __init__.py
├── directory/                  # Main app
│   ├── models.py              # Database models (Category, Page)
│   ├── forms.py               # Django forms
│   ├── views.py               # View logic
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   ├── templates/directory/   # HTML templates
│   └── migrations/            # Database migrations
├── static/css/
│   └── style.css              # Professional stylesheet
├── manage.py                  # Django management script
└── db.sqlite3                 # SQLite database
```

## Setup Instructions

### 1. Navigate to project directory
```bash
cd /home/WP_C1/Desktop/LABS/Lab10/q1/directory_project
```

### 2. Create and activate virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Create database migrations
```bash
python manage.py makemigrations
```

### 5. Apply migrations to database
```bash
python manage.py migrate
```

### 6. Create superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 7. Run development server
```bash
python manage.py runserver
```

### 8. Access the application
- Dashboard: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/

## Database Models

### Category Model
```python
- name (CharField): Category name
- visits (IntegerField): Total visits count
- likes (IntegerField): Total likes count
- created_at (DateTimeField): Creation timestamp
```

### Page Model
```python
- category (ForeignKey): Reference to Category
- title (CharField): Page title
- url (URLField): Website URL
- views (IntegerField): Page view count
- created_at (DateTimeField): Creation timestamp
```

## Application URLs

### Dashboard
- `/` - Main dashboard with statistics

### Category Management
- `/categories/` - List all categories
- `/category/<id>/` - View category details
- `/category/new/` - Create new category
- `/category/<id>/edit/` - Edit category
- `/category/<id>/delete/` - Delete category

### Page Management
- `/pages/` - List all pages
- `/page/<id>/` - View page details
- `/page/new/` - Create new page
- `/page/<id>/edit/` - Edit page
- `/page/<id>/delete/` - Delete page

## Using Django Commands

### Create migrations after model changes
```bash
python manage.py makemigrations
```

### Apply pending migrations
```bash
python manage.py migrate
```

### Create superuser for admin
```bash
python manage.py createsuperuser
```

### Run tests
```bash
python manage.py test
```

### Clear database and start fresh
```bash
python manage.py flush
```

### Interactive Python shell
```bash
python manage.py shell
```

### Collect static files for production
```bash
python manage.py collectstatic
```

## Form Features

### CategoryForm (forms.py)
- Name field with validation
- Visits counter
- Likes counter
- Custom styling with form-control classes

### PageForm (forms.py)
- Category selection dropdown
- Title field with validation
- URL field with validation
- Views counter
- Custom styling with form-control classes

## Features Overview

1. **Dashboard**: Overview of all statistics with quick links
2. **Category Listing**: Grid view of all categories with stats
3. **Category Detail**: View pages within a category
4. **Page Management**: Create, edit, delete pages with URL validation
5. **Statistics**: Auto-increment visits when viewing category details
6. **Auto-tracking**: Page views increment when accessed
7. **Responsive Design**: Works on desktop and mobile devices

## Professional Styling

The CSS is designed to be:
- Clean and minimalist
- Professional appearance
- High readability
- Responsive to all screen sizes
- Color scheme: Blue/grey with red accents
- No unnecessary animations or effects

## Admin Panel

Access Django admin at `/admin/`:
- Manage Categories: Name, visits, likes
- Manage Pages: Title, URL, category, views
- Search and filter functionality
- Bulk actions

## Notes

- All statistics (visits, likes, views) are tracked automatically where applicable
- Page views increment each time the page is accessed
- Category visits increment when viewing a category detail
- All forms include proper validation and error handling
- Database uses SQLite3 for simplicity and portability
