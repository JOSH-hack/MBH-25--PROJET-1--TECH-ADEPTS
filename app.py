import flask
from flask import request
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == 'admin@gmail.com' and password == '123465':
            return render_template('dashboard.html')

        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)