from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route("/") #url http://127.0.0.1:5000/
def home():
    return "Hello! this is the main page <h1>HELLO</h1>"

@app.route("/<name>") #http://127.0.0.1:5000/<name>  name is a parameter e.i - #http://127.0.0.1:5000/nabina
def user(name):
    return f"<h1>hello {name}</h1>" #name will be raplaced to nabina e.i - hello nabina
@app.route("/admin")
# def admin():
#     return redirect(url_for("home")) #it will redirect to home function when the url is #http://127.0.0.1:5000/admin


def admin():
    return redirect(url_for("user",name="Admin!")) #it will redirexct to the admine sector when the name is admin

if __name__ == "__main__":
    app.run()