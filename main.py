#!/usr/bin/python3
"""
Flask Webserver
JakeNTech
2021
"""
from flask import Flask, jsonify
from datetime import datetime
from api import py_api 
import subprocess

app = Flask(__name__)

@app.route('/')
def load_index():
    return app.send_static_file('index.html')

@app.route('/assets/js/<file>')
def send_js(file):
    js_path = "assets/js/"+file
    return app.send_static_file(js_path)

@app.route('/assets/css/<file>')
def send_css(file):
    css_path = "assets/css/"+file
    return app.send_static_file(css_path)

@app.route('/assets/img/<file>')
def send_img(file):
    img_path = "assets/img/"+file
    return app.send_static_file(img_path)

@app.route('/api/<action>',methods=['GET'])
def current_time(action):
    return py_api.request(action)

if __name__ == "__main__":
    app.run()