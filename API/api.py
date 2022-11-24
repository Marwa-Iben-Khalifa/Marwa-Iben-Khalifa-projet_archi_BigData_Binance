import pandas as pd
import json
import flask
from flask import render_template, send_from_directory
from flask import Flask, request
from mongoDbConnection import get_all_data

# FLASK
app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/api/stock', methods=['GET'])
def buys_predict():
    coin = request.args.get('coin')
    return json.dumps(get_all_data(coin))

app.run()