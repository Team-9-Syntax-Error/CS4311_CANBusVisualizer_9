from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from config_handler import ConfigHandler

app = Flask(__name__)

today = date.today()
today = today.strftime("%m/%d/%Y")

ch = ConfigHandler()


@app.route("/")
def main_page():
    return render_template("main_page.html")


# Just in case we dont have "/main_page"
# This one does nothing - Victor Herrera
@app.route("/home")
def home():
    return render_template("home_page.html")


# Project Page
@app.route("/project")
def project_page():
    return render_template("project_page.html")


# Create Projec Page I made these comments for mysef so I dont get confused.- Victor Herrera
@app.route("/create_project")
def create_project():
    return render_template("Create_Project.html", date=today)


# Edit Configuration page
@app.route("/edit_config")
def edit_project():
    return render_template("edit_config.html", date=today)


@app.route("/data_handler", methods=['POST', 'GET'])
def data_handler():
    if request.method == 'POST':
        ch.receive_config_data(request.form)
    return render_template("project_page.html")


if __name__ == "__main__":
    app.run()
