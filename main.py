
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main_page.html")

#Just in case we dont have "/main_page"
@app.route("/main_page")
def main_page():
    return render_template("main_page.html")


@app.route("/create_project")
def create_project():
    return render_template("Create_Project.html")

if __name__ == "__main__":
    app.run()
