# Student Entry App (Lab11/aq1)

## Run

```bash
cd /home/WP_C1/Desktop/LABS/Lab11/aq1
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Open: http://127.0.0.1:8000/

## Features

- Form fields: Student Id, Student Name, Course Name, Date of Birth
- Data saved to SQLite database
- All entered students displayed below form in an unordered list
- Form built using `forms.py` (`StudentForm`)
- Basic HTML and minimal CSS
