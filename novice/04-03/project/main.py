from flask import Flask, render_template, url_for, request
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="QSprogramer2"
    )
    return render_template("index.html", hasil=0)

@app.route("/predict", methods=["POST"])
def predict():
    data1=float(request.form["variable1"])
    data2=float(request.form["variable2"])
    y=data1+data2

    return render_template("index.html", hasil=y)

if __name__ == "__main__":
    app.run()