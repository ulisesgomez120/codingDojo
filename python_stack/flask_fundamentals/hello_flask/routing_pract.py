from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"
@app.route('/dojo')
def dojo():
    return "Dojo"
@app.route('/say/<name>')
def say(name):
    return "hi " + name
@app.route('/repeat/<num>/<string>')
def repeat(num, string):
    return (string + " ") * int(num)

if __name__=="__main__":
    app.run(debug=True) 