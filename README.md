# Football Daily

A Django-based football news website featuring match previews, transfer news, and league information.

## Features

- Football news articles
- Match previews
- Transfer news
- League information
- Admin panel for content management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/arbabmehmood098/footballdaily.git
cd footballdaily
```

2. Create a virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Requirements

- Python 3.11+
- Django 5.2.6+
- Pillow
- WhiteNoise
- Gunicorn

## License

This project is private and proprietary.

