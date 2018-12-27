from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "supersecret"
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=["post"])
def process():
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    name_regex = re.compile(r'\d+')
    password_regex = re.compile(r'[A-Z0-9]+')
    for field in request.form:
        if len(request.form[field]) == 0:
            flash('Field is required', field)
    if len(request.form['first_name']) < 2:
        flash('Name must be at least two letters long', 'first_name')
    elif name_regex.search(request.form['first_name']):
        flash('Can only contain Non-digit characters', 'first_name')
    if len(request.form['last_name']) < 2:
        flash('Name must be at least two letters long', 'last_name')
    elif name_regex.search(request.form['last_name']):
        flash('Can only contain Non-digit characters', 'last_name')
    if not email_regex.match(request.form['email']):
        flash('Must enter a vaild email', 'email')
    if len(request.form['password']) < 8 or len(request.form['password']) > 16:
        flash('Length must be 8-16 characters long', 'password')
    if not password_regex.search(request.form['password']):
        flash('Must contain at least one upper case letter and number', 'password')
    if request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match', 'confirm_password')
# return to homepage if any errors in form
    if "_flashes" in session:
        return redirect('/')
# validate that email is unique
    sql = connectToMySQL("logindb")
    data = {"email": request.form['email']}
# if email not in db, then create
    if not sql.query_db("SELECT email FROM users WHERE email = %(email)s", data):
        sql = connectToMySQL("logindb")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
        }
        user_id = sql.query_db(query,data)
        session["user_id"] = user_id
        session["name"] = request.form['first_name']
        session['login'] = True
        flash('You have been logged in', 'register')
        return redirect('/success')
    else:
        flash('You could not be registered', 'register')
        return redirect('/')
        
@app.route('/login', methods=['post'])
def login():
    if "user_id" in session and 'login' in session:
        session.clear()
    sql = connectToMySQL('logindb')
    query = "SELECT id, first_name, email, password FROM users WHERE email = %(email)s"
    data = {"email": request.form['email']}
    user_list = sql.query_db(query, data)
    if not user_list:
        flash("You were not logged in", "login")
        return redirect('/')
    else:
        user = user_list[0]
        if bcrypt.check_password_hash(user['password'], request.form['password']):
            session["user_id"] = user['id']
            session["name"] = user['first_name']
            session['login'] = True
            flash('You were successfully logged in', 'login')
            return redirect('/success')
        else:
            flash('Email or password was incorrect', 'login')
            return redirect('/')

@app.route('/success')
def success():
    if "user_id" not in session and "login" not in session:
        flash("You are not logged in", "login")
        return redirect('/')
    return render_template('success.html')

@app.route('/logout', methods=['post'])
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)