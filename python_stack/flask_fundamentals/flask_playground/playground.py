from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>try /play</h1>"

@app.route('/play')
def boxes():
    return render_template("playground_index.html",num = 3)
@app.route('/play/<num>')
def more_boxes(num):
    to_int = int(num)
    return render_template("playground_index.html",num=to_int)
@app.route('/play/<num>/<color>')
def colored_boxes(num,color):
    to_int = int(num)
    return render_template("playground_index.html",num=to_int,color=color)

if __name__ == "__main__":
    app.run(debug=True)