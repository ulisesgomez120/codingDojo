from flask import Flask, render_template
from mysqlconnection import connectToMySQL


app = Flask(__name__)

@app.route('/')
def home():
    sql = connectToMySQL("lead_clients")
    query = "SELECT CONCAT(first_name, ' ', last_name) AS name, COUNT(leads.name) AS number_of_leads FROM customers JOIN leads ON customers.id = leads.customer_id GROUP BY customers.id;"
    customers = sql.query_db(query)
    print("-" * 80)
    print(customers)
    return render_template("index.html", customers=customers)

if __name__ == "__main__":
    app.run(debug=True)