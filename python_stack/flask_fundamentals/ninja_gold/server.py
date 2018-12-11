from flask import Flask, render_template, redirect, request, session
import random, datetime, time

app = Flask(__name__)
app.secret_key = "SuperSecret"

@app.route('/')
def home():
    if "your_gold" not in session:
        session["your_gold"] = 0
    if "activity" not in session:
        session["activity"] = ["Let's get some Gold!"]
    
    print("------home-------\n", session)
    return render_template("index.html")

@app.route('/process_money', methods=["post"])
def process():
    date = datetime.datetime.today()
    if request.form["building"] == "farm":
        gold = random.randint(10,20)
        session["your_gold"] += gold
        message = f"<p class='won'>Earned {gold} gold from the {request.form['building']}! ({date})</p>"
    if request.form["building"] == "cave":
        gold = random.randint(5,10)
        session["your_gold"] += gold
        message = f"<p class='won'>Earned {gold} gold from the {request.form['building']}! ({date})</p>"
    if request.form["building"] == "house":
        gold = random.randint(2,5)
        session["your_gold"] += gold
        message = f"<p class='won'>Earned {gold} gold from the {request.form['building']}! ({date})</p>"
    if request.form["building"] == "casino":
        win_lose = random.randint(0,1)
        gold = random.randint(0,50)
        if win_lose == 0:
            session["your_gold"] -= gold
            message = f"<p class='loss'>Entered a casino and lost {gold} gold... Ouch! ({date})</p>"
        else:
            session["your_gold"] += gold
            message = f"<p class='won'>Entered a casino and won {gold} gold! ({date})</p>"
    session["activity"].append(message)
    print("------process-------\n", session)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)