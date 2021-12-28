import os
from flask import Flask, redirect, request, render_template, url_for, session

from interact_with_DB import interact_db

app = Flask(__name__)

users = [
    {'username': 'aviv', 'email': 'aviv@gmail.com', 'password': ''},
    {'username': 'eitan', 'email': 'eitan@gmail.com', 'password': ''},
    {'username': 'moshe', 'email': 'moshe@gmail.com', 'password': ''},
    {'username': 'shay', 'email': 'shay@gmail.com', 'password': ''},
    {'username': 'itay', 'email': 'itay@gmail.com', 'password': ''},
    {'username': 'dekel', 'email': 'dekel@gmail.com', 'password': ''}
]


@app.route("/")
def home():
    return render_template('assignment9.html', users=users)


@app.route("/registration/")
def registration():
    return render_template('registration.html')


@app.route("/search_user/")
def search_user():
    search_username = None
    search_email = None
    if len(request.args) > 0:
        search_username = request.args["username"]
        search_email = request.args["email"]
    return render_template('assignment9.html', users=users, username=search_username, email=search_email, searchValid=1)


@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    session['username'] = name
    users.append({'username': name, 'email': email, 'password': password})
    return redirect(url_for('home'))


@app.route('/logout', methods=['POST'])
def logout():
    if session['username']:
        username = session['username']
        if username in users:
            users.pop(username)
        session.pop('username')
    return redirect(url_for('registration'))


if __name__ == '__main__':
    #   Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.secret_key = '12345'
    app.run(host='0.0.0.0', port=port)
