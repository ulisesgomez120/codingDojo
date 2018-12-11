from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "lokiodinson"

@app.route('/')
def home():
    print("---home---")
    if "my_num" not in session:
        session["my_num"] = random.randrange(1,100)
    if "message" not in session:
        session["message"] = ''
    if "class" not in session:
        session["class"] = ''
    print(session)
    return render_template('index.html', **locals())

@app.route('/check', methods=["post"])
def check():
    print("---check---")
    print(session)
    print(request.form)
    if session["my_num"] == int(request.form["player_num"]):
        session["message"] = f"{session['my_num']} was right!"
        session["class"] = "right"
        return redirect('/')
    if session["my_num"] > int(request.form["player_num"]):
        session["message"] = f"Too Low"
        session["class"] = "low"
        return redirect('/')
    if session["my_num"] < int(request.form["player_num"]):
        session["message"] = f"Too High"
        session["class"] = "high"
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    print(session)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

