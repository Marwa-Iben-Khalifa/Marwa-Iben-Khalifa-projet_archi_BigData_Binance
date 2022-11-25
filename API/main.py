import pandas as pd
import json
import flask
from flask import render_template, send_from_directory
from flask import Flask, request
from mongoDbConnection import get_all_data

# FLASK
app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/api/stock', methods=['GET'])
def buys_predict():
    coin = request.args.get('coin')
    return get_all_data(coin)
