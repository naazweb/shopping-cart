### Description
This REST API is built with Django REST Framework.


### Setup Locally
1. Clone Repository and checkout to `dev` branch.

    `git clone https://github.com/naazweb/shopping-cart`

    `cd shopping-cart` (move to the repo)

2. Setup virtual environment

    `python -m venv env` 
   
    or
    
    `virtualenv env`
3. Activate virtual environment

    `env/scripts/activate`

    or Linux / Mac
    
    `source env/bin/activate`
4. Install requirements

    `pip install -r requirements.txt`
5. Migrate and Run

    `python manage.py migrate`

    `python manage.py runserver`

6. Server will be up at http://127.0.0.1:8000/


##### Thanks for stopping by ^ __ ^