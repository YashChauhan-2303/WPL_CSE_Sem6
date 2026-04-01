# Quick Start - Human Management System

## Start the Server

```bash
cd /home/WP_C1/Desktop/LABS/Lab11/q3
python3 manage.py runserver
```

Open: http://127.0.0.1:8000/

## Load Sample Data

To quickly populate the database with 5 test records:

```bash
python3 manage.py load_sample_data
```

This adds:
- John Doe (555-1234, 123 Main St, New York)
- Jane Smith (555-5678, 456 Oak Ave, Los Angeles)
- Bob Johnson (555-9012, 789 Pine Rd, Chicago)
- Alice Williams (555-3456, 321 Elm St, Houston)
- Charlie Brown (555-7890, 654 Maple Dr, Phoenix)

## How to Use

### Method 1: Add New Person (No Sample Data Needed)
1. Fill in the "Add New Person" form at the top
2. Click "Add Person"
3. The new person will appear in the dropdown

### Method 2: Use Sample Data
1. Run `python3 manage.py load_sample_data`
2. The dropdown will show all first names
3. Select a name to see their details
4. Click Update to modify fields
5. Click Delete to remove the record

## Functionality

- **Add Form** - Create new people directly from the main page
- **Dropdown** - Loads with all first names (automatically updates after add/delete)
- **Select** - Choose a person to see their details
- **Edit** - Modify the text fields
- **Update** - Save changes to database
- **Delete** - Remove the record (with confirmation)

## Form Elements

- **Add Form** (at top)
  - First Name, Last Name, Phone, Address, City textboxes
  - "Add Person" button
  
- **Selection Section** (middle)
  - Dropdown showing all first names
  - Auto-submits on selection
  
- **Details Section** (bottom)  
  - Text boxes showing selected person's details
  - "Update" button - posts to `/update/`
  - "Delete" button - posts to `/delete/` with confirmation

## Database Tables

```
Human
├── id (PK)
├── first_name
├── last_name
├── phone
├── address
└── city
```

## URL Routes

- `/` - Main page (GET: display form, POST: load person details)
- `/add/` - Add new person (POST)
- `/update/` - Update person (POST)
- `/delete/` - Delete person (POST)

## Notes

- The dropdown auto-submits using `onchange="this.form.submit()"`
- Delete action shows a confirmation dialog
- You can add people without sample data
- All form validation is handled by Django forms
