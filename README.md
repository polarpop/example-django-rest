# Example API

This is a very simplistic API utilizing django and djangorestframework.

1. Create a abstract user model.
2. Create a location model.
3. Create a user serializer.
4. Create a location serializer.
5. Create a viewset for each serializer.
6. Create a default router with each viewset given a route.


## Objectives

1. Give you a basic understanding of how django works.
2. Basic understanding of API's.


## Assignment??? Nah, seriously homework???

1. Create an API client for both Users and Location.
2. Create permissions so only certain people can view users, or create users.
3. Connect to a different database besides SQLite

### Resources

1. [Rest Framework Permissions](http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
2. [HTTP Requests in Python](http://docs.python-requests.org/en/master/)
3. [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

## Installation & requirements

### Requirements

[Python 3.6>](https://www.python.org/downloads/release/python-370/)


### Installation
	Run the following commands
	`py -m "pip" install virtualenv`
	`virtualenv myapp`
	`cd myapp`
	`Scripts\activate`
	`pip install django djangorestframework django-cors-headers`
	`git clone https://github.com/polarpop/example-django-rest example`
	`cd example`
	`python manage.py makemigrations`
	`python manage.py migrate`
	`python manage.py loaddata initial`