import os
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/walla')
def walla_site():
    return redirect("http://news.walla.co.il")


@app.route('/walla/index')
def walla_site_index():
    return redirect(url_for("walla_site"))


@app.route('/google')
def google_site():
    return redirect("http://google.com")


@app.route('/google/index')
def google_site_index():
    return redirect(url_for("google_site"))


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)

