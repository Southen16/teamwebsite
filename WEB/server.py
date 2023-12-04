from flask import Flask, render_template, request, redirect, url_for
from utility import check,insert

app = Flask(__name__)


@app.route('/')
def index(name=""):
    return render_template('index.html',name=name)
@app.route('/login_page')
def loginpage():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if check(username,password):
        print(username)
        return render_template('index.html',name=username)
    else:
        # In a real scenario, you'd handle failed login attempts more gracefully
        return "Invalid username or password. <a href='/'>Back to login</a>"

@app.route('/signup', methods=['POST'])
def signup():
    fullname = request.form['fullname']
    email = request.form['email']
    new_username = request.form['new_username']
    new_password = request.form['new_password']
    insert(fullname,email,new_username,new_password)
    return render_template('login.html')

@app.route('/success')
def success():
    return "Login or signup successful!"

if __name__ == '__main__':
    app.run("0.0.0.0",port=80)
