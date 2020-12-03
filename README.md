# Django_readymade

Django_readymade is a simple starter template for django project. These are the following things included inside the project:

+ asgiref==3.3.1
+ Django==3.1.4
+ pytz==2020.4
+ sqlparse==0.4.1
+ django-debug-toolbar==3.1.1
+ python-decouple==3.3
+ Bootstrap == 4.5
+ rename.py file (Note:  Rename your project with python manage.py rename <yourprojectname> <newprojectname> )
+ Hero as apps in django
+ core as custom django command
  
# Settings files
+ base.py - 
Settings common to all instances of the project.

+ local.py - 
This is the settings file that you use when you’re working on the project locally.
Local development-specific settings include DEBUG mode, log level, and
activation of developer tools like django-debug-toolbar.

+ staging.py - 
Staging version for running a semi-private version of the site on a production
server. This is where managers and clients should be looking before your work is
moved to production.

+ test.py - Settings for running tests including test runners, in-memory database
definitions, and log settings.

+ production.py -
This is the settings file used by your live production server(s). That is, the
server(s) that host the real live website. This file contains production-level
settings only. It is sometimes called prod.py.

# Create .env file and generate secret key
1. add .env file 
2. copy from .demo_env_template and paste in .env file
3. Generate Secret_key in python shell:
- $ python manage.py shell -c 'from django.core.management import utils;print(utils.get_random_secret_key())'
4. copy key and add to SECRET KEY in .env file

# How to rename project
1. open terminal and write:
> ```python manage.py rename myproject <yourprojectname>```
2. hit enter
