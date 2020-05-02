# Django Addons Demos

## Installation

```shell
git clone https://github.com/srault95/demos-django-addons.git
cd demos-django-addons
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-base.txt

# optional:
pip install -r requirements-pgsql.txt
```

## django-polymorphic example

```shell
cd django-polymorphic
pip install -r requirements.txt

# Apply migrate
./manage.py migrate

# load default admin account (login: admin/ password: pass)
./manage.py loaddata ../fixtures/superuser.json

# Run server:
./manage.py runserver --insecure 127.0.0.1:8000
```

## Use with Docker

- TODO...

## Use PostgreSQL

- TODO...

## Use MySQL

- TODO...

## Addons

| Name                      | Directory                                 | Status  |
| -------------             |:-------------:                            | -----:|
| [django-polymorphic]      | [django-polymorphic/](django-polymorphic) | OK |


[django-polymorphic]: https://github.com/django-polymorphic/django-polymorphic