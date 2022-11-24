import flask
from create_routes import create_routes

Dev = True

# Initialize flask
app = flask.Flask(__name__)
app.config["DEBUG"] = Dev

# Set headers json for all requests


@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# Import routes
create_routes(app)

app.run()
