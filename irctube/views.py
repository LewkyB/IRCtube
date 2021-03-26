import json
import os

from flask import render_template

from irctube import app


@app.route('/')
def index():
    
    # get correct file path for json file
    here = os.path.dirname(os.path.abspath(__file__))
    server_channel_json_file = os.path.join(here, 'server_channel_info.json')
    
    with open(server_channel_json_file, "r") as fp:
        irc_servers = json.load(fp)
    return render_template('home.html', irc_servers=irc_servers)


@app.route('/videos/<server_name>/<channel_name>')
def get_chat_videos(server_name, channel_name):
    
    # get correct file path for json file
    here = os.path.dirname(os.path.abspath(__file__))
    irc_info_and_links_json_file = os.path.join(here, 'irc_info_and_links.json')
    
    with open(irc_info_and_links_json_file, "r") as fp:
        servers_channels_links = json.load(fp)

    videos = []

    for block in servers_channels_links:
        if block['server'] == server_name and block['chatroom'] == channel_name:
            videos.append(block)

    return render_template('chatroom_videos.html', videos=videos, server_name=server_name, channel_name=channel_name)
