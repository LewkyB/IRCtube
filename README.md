# IRCtube #

Videos from IRC

## Requirements ##

* gunicorn
* flask

## Installing ##

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Running locally ##

    FLASK_DEBUG=TRUE FLASK_APP=irctube flask run

## Running tests ##

    python setup.py test
