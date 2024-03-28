# FIDS2# Just for practice and to remember
To create a Django project first of all, I had created a Virtual environment(V.E) using, pipenv.
After that, in my virtual environment, I installed Django using "pip install django" command.
After it's installation, to confirm whether it is installed or not, typed "pip show django" and it showed my django version.

Now that django is ready, I start a new project in my V.E using command "django-admin startproject Display" and it created a new project named Display for me.

I then, created an app using, with "django-admin starapp Feed" command, and an App named Feed was created.
I have, created a superuser, "django-admin createsuperuser" command.
I then, go to setting.py file of my project and in "Installed App"  portion, entered my App name.
Then, I opened my models.py file, I have created different classes for my database model and run following commands. i.e "python manage.py makemigrations" and then "python manage.py migrate"
Then I registered these model classes with my admin.py file, to control these model classes from admin site.



