from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/") #url http://127.0.0.1:5000/
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()