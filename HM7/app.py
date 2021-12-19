from flask import Flask
from flask import redirect, url_for, render_template
app=Flask(__name__)

@app.route('/catalog')
def catalog_func():
        return render_template('catalog')
if __name__ == '__main__':
    app.run(debug=True)