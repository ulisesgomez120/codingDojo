from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def display_results():
    print(request.form)
    return render_template("result.html")

@app.route('/danger')
def nope():
    print("a user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)