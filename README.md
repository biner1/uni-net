# About
    A simple website for uploading lectures, viewing it, and voting for the lectures,
    a moderator can upload lectures, a registered account can vote for the lectures of his stage.
    this webApp was created only using starter django concepts to show
    my progress of learning django.
    VERY BAD FRONTEND


# Plan
    I will try to improve the webApp by adding more features...
    and maybe add some styleing to the webApp or rebuild the website in a more advanced way.




# Requirements
python==3.x
pip==latest version
asgiref==3.4.1
beautifulsoup4==4.10.0
dj-database-url==0.5.0
Django==3.2.7
django-appconf==1.0.5
django-crispy-forms==1.12.0
django-heroku==0.3.1
django-imagekit==4.0.2
gunicorn==20.1.0
pilkit==2.0
Pillow==8.3.2
psycopg2==2.9.1
pytz==2021.1
six==1.16.0
soupsieve==2.2.1
sqlparse==0.4.1
whitenoise==5.3.0



# Install and run

Make sure you have Python 3.x installed and the latest version of pip installed before running these steps.

-Clone the repository using the following command

git clone git@github.com:biner1/uni-net.git

-After cloning, move into the directory having the project files using the change directory command
cd uni-net


-Create a virtual environment where all the required python packages will be installed

# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env

-Activate the virtual environment

# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate

-Install all the project Requirements

pip install -r requirements.txt

-Add Secret_key in the settings file

-Apply migrations and create your superuser (follow the prompts)

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser


-Run the development server

# run django development server
python manage.py runserver


Explore admin panel for model data or instances

http://127.0.0.1:8000/admin or http://localhost:8000/admin