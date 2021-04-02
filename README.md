# IRCtube #

Parse IRC chat logs from [The Lounge](https://github.com/thelounge/thelounge) for youtube links then display them on a website for easy browsing.
 
<p align="center">
    <img width="400" alt="front page" src="https://i.imgur.com/oygzs8y.png">
    <img width="340" alt="front page" src="https://i.imgur.com/Av4d0Yj.png">
</p>

## Requirements ##

* gunicorn
* flask

## Installing ##

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Running locally ##

    FLASK_DEBUG=TRUE FLASK_APP=irctube flask run

## Updating the JSON files for new links ##

Use yt_irc_sqlite.py to parse logs and produce JSON files `irc_info_and_links.json` `server_channel_info.json` 
    
    $ python yt_irc_sqlite.py ~/.thelounge/logs/luke.sqlite3 ~/.thelounge/users/luke.json
    $ mv irc_info_and_links.json irctube/irc_info_and_links.json
    $ mv server_channel_info.json irctube/server_channel_info.json

## Running tests ##

    python setup.py test
    
