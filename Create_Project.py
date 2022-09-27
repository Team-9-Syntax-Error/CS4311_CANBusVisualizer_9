
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/create_project")
def home():
    return render_template("Create_Project.html")

if __name__ == "__main__":
    app.run()