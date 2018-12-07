from flask import Flask, redirect,render_template,request,session
app = Flask(__name__)
app.secret_key = "Super_Secret"

@app.route('/')
def home():
    if 'count' not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html', count=session["count"] )

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")

@app.route('/add2', methods=["post"])
def add():
    session["count"] += 1
    return redirect('/')

@app.route('/reset', methods=["post"])
def reset():
    return redirect("/destroy_session")


if __name__ == "__main__":
    app.run(debug=True)