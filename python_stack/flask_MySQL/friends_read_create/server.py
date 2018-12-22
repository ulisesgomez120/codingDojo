from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def home():
    mysql = connectToMySQL("friendsdb")
    all_friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends = all_friends)

@app.route('/friend/add', methods=['post'])
def create():
    errors = []
    if len(request.form["first_name"]) < 2:
        errors.append("First name most be at least 2 letters")
    if len(request.form["last_name"]) < 2:
        errors.append("Last name most be at least 2 letters")
    if len(request.form["occupation"]) < 2:
        errors.append("Occupation most be at least 2 letters")
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')    
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    new_user_id = mysql.query_db(query,data)    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)