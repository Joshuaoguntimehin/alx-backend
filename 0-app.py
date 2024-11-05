#!/usr/bin/env python3
"""import statement"""
from flask import Flask, render_template 
from flask_babel import Babel

app = Flask(__name__)

@app.route("/")
def nothing():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()