from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "supersecret"
bcrypt = Bcrypt(app)

@app.route('/')
def home():   
    if "user_id" not in session and "login" not in session:
        flash("You are not logged in", "login")
        return redirect('/login_register')
    
    sql = connectToMySQL('walldb')
    # select all messages
    get_messages = f"SELECT received, sent, users2.first_name, content, messages.created_at FROM users JOIN messages ON users.id = messages.received JOIN users AS users2 ON messages.sent = users2.id WHERE users.id = {session['user_id']};"
    messages = sql.query_db(get_messages)
    # select all users not logged in
    sql.connection.ping()
    get_users = f"SELECT id, first_name FROM users WHERE id != {session['user_id']};"
    users = sql.query_db(get_users)
    
    return render_template('dashboard.html', **locals())

@app.route('/login_register')
def login_register():
    return render_template('login_register.html')

@app.route('/register', methods=["post"])
def process():
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    name_regex = re.compile(r'\d+')
    password_regex = re.compile(r'[A-Z0-9]+')
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
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
        return redirect('/login_register')
# clear saved form data
    session.clear()
# validate that email is unique
    sql = connectToMySQL("walldb")
    data = {"email": request.form['email']}
# if email not in db, then create
    if not sql.query_db("SELECT email FROM users WHERE email = %(email)s", data):
        sql = connectToMySQL("walldb")
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
        return redirect('/')
    else:
        flash('You could not be registered', 'register')
        return redirect('/login_register')
        
@app.route('/login', methods=['post'])
def login():
    if "user_id" in session and 'login' in session:
        session.clear()
    session["email_login"] = request.form["email_login"]
    sql = connectToMySQL('walldb')
    query = "SELECT id, first_name, email, password FROM users WHERE email = %(email)s"
    data = {"email": request.form['email_login']}
    user_list = sql.query_db(query, data)
    if not user_list:
        flash("You were not logged in", "login")
        return redirect('/login_register')
    else:
        session.clear()
        user = user_list[0]
        if bcrypt.check_password_hash(user['password'], request.form['password_login']):
            session["user_id"] = user['id']
            session["user_name"] = user['first_name']
            session['login'] = True
            return redirect('/')
        else:
            flash('Email or password was incorrect', 'login')
            return redirect('/login_register')

@app.route('/send_message', methods=['post'])
def send_message():
    sql = connectToMySQL('walldb')
    query = "INSERT INTO messages(received, sent, content, created_at, updated_at) VALUES (%(received)s, %(sent)s, %(content)s ,now(),now());"
    data = {
        "received": request.form['received_id'],
        "sent": session['user_id'],
        "content": request.form['message']
    }
    sql.query_db(query,data)
    flash('Message sent')
    return redirect('/')

@app.route('/delete_message/<id>')
def delete_message(id):
    if 'user_id' not in session:
        flash('You are not logged in', 'login')
        return redirect('login_register')
    sql = connectToMySQL('walldb')
    get_message = "SELECT received, sent FROM users JOIN messages ON users.id = messages.received JOIN users AS users2 ON messages.sent = users2.id WHERE messages.id = %(id)s;"
    data = { "id": id}
    message = sql.query_db(get_message,data)
    if message[0]['received'] != session['user_id']:
        return redirect('/danger')
    else:
        sql.connection.ping()
        delete = "DELETE FROM messages WHERE id = %(id)s"
        sql.query_db(delete,data)
        return redirect('/')

@app.route('/danger')
def danger():
    if "visits" not in session:
       session["visits"] = 1
    if session["visits"] > 1:
        session.clear()
        return redirect('/login_register')
    session["visits" ] += 1
    return render_template('danger.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login_register')

if __name__ == "__main__":
    app.run(debug=True)

# create messages
# 



