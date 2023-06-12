# Django Rules API Backend

This is a simple Django-based API backend for managing language rules and examples.

### Step 1: Clone the repository

```bash
git clone https://github.com/prgmlu/arabic-grammar-backend.git
;cd arabic-grammar-backend;
python3 -m venv env
```

On Windows, use env\Scripts\activate
On Unix or MacOS, use source env/bin/activate

init, create admin user:
```bash
pip install -r requirements.txt;
manage.py makemigrations;
python manage.py migrate;
python manage.py populate_db;
python manage.py createsuperuser;
python manage.py runserver
```

The Django Admin Interface can be accessed at http://127.0.0.1:8000/admin/.

The API will be served at http://127.0.0.1:8000/. You can access the API at http://127.0.0.1:8000/api/rules/.
