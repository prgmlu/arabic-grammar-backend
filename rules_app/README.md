# Django Rules API Backend

This is a simple Django-based API backend for managing language rules and examples.

### Step 1: Clone the repository

```bash
git clone <your-repository-link>

Step 2: Create a virtual environment
Navigate into the project directory and create a Python virtual environment:

cd <your-project-name>
python3 -m venv env

Activate the virtual environment:

On Windows, use env\Scripts\activate
On Unix or MacOS, use source env/bin/activate
Step 3: Install the dependencies
After you've activated the virtual environment, install the project dependencies with:

pip install -r requirements.txt

python manage.py migrate

python manage.py populate_db

python manage.py createsuperuser
The Django Admin Interface can be accessed at http://127.0.0.1:8000/admin/.

python manage.py runserver

The API will be served at http://127.0.0.1:8000/. You can access the API at http://127.0.0.1:8000/api/rules/.
