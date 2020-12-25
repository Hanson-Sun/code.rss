from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index.html")
def index():
    return render_template("index.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)