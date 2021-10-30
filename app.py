import os
from urllib.request import urlretrieve as retrieve
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)


# Function to display our home page
@app.route('/')
def index():
    return render_template('index.html')


app.secret_key = 'some_secret_key'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)