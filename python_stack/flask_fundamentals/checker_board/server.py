from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def stand_board():
    return render_template("index.html",x=8,y=8)

@app.route('/<x>/<y>')
def custom_board(x,y):
    x_int = int(x)
    y_int = int(y)
    return render_template("index.html",x=x_int, y=y_int)

if __name__ == "__main__":
    app.run(debug=True)