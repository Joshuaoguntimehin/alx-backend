#!/usr/bin/env python3
"""import statement"""
from flask import Flask, render_template,request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

app.config['DEFAULT_TIMEZONE'] = 'UTC'
app.config['BABEL_DEFAULT_LOCATE'] = "en"
app.config['BABEL_SUPPORTED_LOCALES'] = ["en", "fr"]

def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)