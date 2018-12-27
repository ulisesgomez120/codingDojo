from flask import Flask, render_template,redirect,request,session,flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/validate', methods=['post'])
def validate():
# check if email is valid
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    errors = []
    if not email_regex.match(request.form['email']):
        errors.append('Must be a valid email!')
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
# check if email already exists 
    sql = connectToMySQL('emailvalidate')
    data = { "email": request.form['email'] }
    email_dic = sql.query_db('SELECT email FROM users WHERE email = %(email)s', data)
    if email_dic:
        errors.append('Email already exists')
    else:
        sql.connection.ping()
        query = "INSERT INTO users(email, created_at, updated_at) VALUES (%(email)s, now(), now())"
        sql.query_db(query,data)    
    if errors:
        for error in errors:
            flash(error)
        return redirect('/') 
    return redirect('/success')

    
    


@app.route('/success')
def success():
    sql = connectToMySQL('emailvalidate')
    emails = sql.query_db('SELECT email, created_at FROM users')
    return render_template('success.html', users=emails)

@app.route('/delete', methods=['post'])
def delete():
    sql = connectToMySQL('emailvalidate')
    query = "DELETE FROM users WHERE email = %(email)s"
    data = { "email": request.form['email']}
    sql.query_db(query,data)
    return redirect('/success')
    
if __name__ == "__main__":
    app.run(debug=True)