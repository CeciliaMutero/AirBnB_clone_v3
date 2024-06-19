#!/usr/bin/python3
"""modularize my API"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """Defines the function to be called"""
    return jsonify({"status": "OK"})
