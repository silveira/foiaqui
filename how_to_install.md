#How to install foiaqui in your local machine

# What you need #

We are assuming that you are in a linux machine with an python interpreter installed and a database (mysql in our example). You don't need apache instaled.

# Getting lastest django version #

We are using an developmente version of Django. See [Django Instalation](http://www.djangoproject.com/documentation/install/) to learn how install and SVN version of Django.

# Get the last version of foiaqui #

In terminal do:
```
svn checkout http://foiaqui.googlecode.com/svn/trunk/ foiaqui
```

This will download the last version of foiaqui in the directory named _foiaqui_.

# Set up database #

There are two things to setup in foiaqui, the database and media files.
First, edit the file _setting.py_ and change the value of 4 variables:
```
DATABASE_ENGINE = 'yourdb' # example, mysql
DATABASE_NAME = 'db_name' # example, foiaqui_db
DATABASE_USER = 'username' # example root
DATABASE_PASSWORD = 'password' # example 1234 duh!
```

Change them to fit with your database settings.

# Set up mediafiles #

Now edit the file _url.py_ and search for the line with this content:
```
(r'^mediafiles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/foiaqui/media'}),
```
change '/home/foiaqui/media' for the local where you download the foiaqui and '/media'. Example '/home/silveira/foiaqui/media' or '/tmp/foiaqui/media'.

# Test it #

If everything is ok, try to execute this in the folder where you downloaded foiaqui:
```
./manage.py runserver
```
and point your browser to
```
http://127.0.0.1:8000
```
You should see the aplication running.