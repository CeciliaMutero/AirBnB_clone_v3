#!/usr/bin/python3
""" API initialization """
import sys
import os

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../../')
))


app = Flask(__name__)


app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """cleans up after use"""
    storage.close()


if __name__ == '__main__':
    from os import getenv
    app.run(
            host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', 5000)),
            threaded=True
        )
