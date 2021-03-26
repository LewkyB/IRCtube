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

    > skip steps 1 and 2 if you want to just use the provided json files

    1. Get the json files from .thelounge `python yt_irc_sqlite.py /home/luke/.thelounge/logs/luke.sqlite3 /home/luke/.thelounge/users/luke.json`
    
    2. move `irc_info_and_links.json` and `server_channel_info.json` into `IRCtube/IRCtube/` (sample json already in place)
    
    3. `FLASK_DEBUG=TRUE FLASK_APP=irctube flask run`

## Running tests ##

    python setup.py test
