import os
from flask import Flask, render_template, redirect
from flask import request, session
from interact_with_DB import interact_db

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

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO USERES (name ,email,password) values )('%s','%s','%s')" % ({name},{email},{password})
    interact_db(query=query, query_type='commit')
    return redirect('/users')

if __name__ == '__main__':
    #   Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
