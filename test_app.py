#!/usr/bin/python3
from flask import Flask, jsonify


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
