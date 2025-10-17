# club-management-backend
Backend for the Club Management System (Django + Python)

# How to contribute
1. Clone the repo
```bash
git clone  https://github.com/APP-Factory-USIU/club-management-backend.git
```

2. Create and activate virtual environment
```bash
# Create a virtual env
python -m venv venv 

# Activate the env
venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
```

3. Install project dependencies
```bash
pip install -r requirements.txt

```
5. Run migration
```bash
python manage.py makemigrations .

python manage.py migrate

```
4. Run the server
```bash
python manage.py runserver
```
