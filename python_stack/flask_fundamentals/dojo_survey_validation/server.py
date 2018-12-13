from flask import Flask, redirect, request, session, flash, render_template
app = Flask(__name__)
app.secret_key = "thunderson"

@app.route('/')
def home():
    location = ["San Jose", "Burbank", "Seatle"]
    languages = ["Python", "JavaScript", "Ruby"]
    if "passed" in session:
        if session["passed"]:
            session.clear()
    print("--------------home",session)
    return render_template('index.html', **locals())

@app.route('/process', methods=["post"])
def process():
    session["passed"] = False
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    errors = False

    if len(request.form["name"]) == 0:
        flash("Name can't be blank", "flash")
        errors = True
    if len(request.form["comments"]) > 120:
        flash("Comments can't be more than 120 characters", "flash")
        errors = True

    print(session)
    if errors:
        return redirect('/')
    else:
        return redirect('/result')

@app.route('/result')
def results():
    session["passed"] = True
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
