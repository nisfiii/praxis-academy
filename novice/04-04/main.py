from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "halo nisfi"

if __name__ == "__main__":
    app.run()