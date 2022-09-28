
from flask import Flask, redirect, url_for, render_template
from datetime import date

app = Flask(__name__)


today = date.today()
today = today.strftime("%m/%d/%Y")

@app.route("/")
def main_page():
    return render_template("main_page.html")

#Just in case we dont have "/main_page"
@app.route("/home")
def home():
    return render_template("home_page.html")


@app.route("/create_project")
def create_project():
    return render_template("Create_Project.html", date=today)

if __name__ == "__main__":
    app.run()
