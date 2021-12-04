#!/usr/bin/python3
"""
Flask Webserver
JakeNTech
2021
"""
from flask import Flask, jsonify
from api import py_api, configure

#Flask App
app = Flask(__name__)

#Send Index.html
@app.route('/')
def load_index():
    return app.send_static_file('index.html')
# Send Files to make index.html look nice and fancy
@app.route('/assets/js/<file>')
def send_js(file):
    js_path = "assets/js/"+file
    return app.send_static_file(js_path)
@app.route('/assets/css/<file>')
def send_css(file):
    css_path = "assets/css/"+file
    return app.send_static_file(css_path)
# Send Graphs
@app.route('/assets/img/temp_graphs/<file>')
def send_img(file):
    img_path = "assets/img/temp_graphs/"+file
    return app.send_static_file(img_path)

# Deal with API requests...by passing them to the other python file and then back to JS.
@app.route('/api/<action>',methods=['GET'])
def api_call(action):
    return jsonify(py_api.api(action))

if __name__ == "__main__":
    #Global Variables for configuration
    configure.init("./config.json")
    app.run()