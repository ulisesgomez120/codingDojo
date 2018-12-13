from flask import Flask, render_template, redirect, request, session, flash
import re
app = Flask(__name__) 
app.secret_key = "supersecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[0-9]')
PASSWORD_REGEX = re.compile(r'[A-Z0-9]+')
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    for name in request.form:
        if len(request.form[name]) == 0:
            flash(f"{name.capitalize()} cannot be blank")
    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email")
    if NAME_REGEX.search(request.form["first_name"]) or NAME_REGEX.search(request.form["last_name"]):
        flash("No numbers accepted in name fields")
    if len(request.form['password']) < 8:
        flash("Password must be more than 8 characters")
    if not PASSWORD_REGEX.search(request.form["password"]):
        flash("Password must have at least 1 uppercase word and at least 1 number")
    if not request.form['password'] == request.form['confirm_password']:
        flash("Passwords don't match")
    print(session)
    if "_flashes" in session:
        return redirect('/')
    else:
        flash("Thanks for submitting your information.","text-success")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)