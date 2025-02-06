import json
from flask import Flask, jsonify, render_template, redirect, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def default():
    return "hi"


if __name__ == '__main__':
    print("running")
    app.run(debug=True, port=4200)