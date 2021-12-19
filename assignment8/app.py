import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('assignment8.html')


@app.route("/home/")
def home_redirect():
    return render_template('assignment8.html')


@app.route("/cv/")
def cv():
    return render_template('cvGrid.html')


@app.route("/register/")
def register():
    return render_template('register.html')


@app.route("/contact/")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    #   Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
