from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from data_handler import DataHandler
import os

app = Flask(__name__)

today = date.today()
today = today.strftime("%m/%d/%Y")

dh = DataHandler()

#Project Page / Table information is comming
headings = ("ID", "Time", "Data")
data = (
    ("123456", "09/30/2022","Data Example 1" ),
    ("987654", "09/30/2022","Data Example 2" ),
    ("456123", "09/30/2022","Data Example 3" ),
)
@app.route("/")
def table():
    return render_template("Project_Page.html", headings=headings, data=data)
# This is our Main Page / First Page that appears
@app.route("/")
def main_page():
    return render_template("main_page.html")


# This handles uploading the project files
# NEEDS REFINEMENT --- LOOK FOR UPLOAD JSON FILES OR PROJECT FOLDER
app.config["UPLOAD_PATH"] = "C:/"


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            # f = request.files['file_name']
            f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
        return render_template("upload_file.html", msg="Project Uploaded Successfully")
    return render_template("upload_file.html", msg="Select Project to Open")


# Project Page
# This is the page where the users is going to be working
@app.route("/project")
def project_page():
    return render_template("project_page.html")


# Create Project Page I made these comments for mysef so I dont get confused.- Victor Herrera
@app.route("/create_project")
def create_project():
    return render_template("Create_Project.html", date=today)


# Edit Configuration page
# When working on the project this will allow the user to modify the configuration
@app.route("/edit_config")
def edit_project():
    return render_template("edit_config.html", date=today)


@app.route("/config_handler", methods=['POST', 'GET'])
def config_handler():
    if request.method == 'POST':
        dh.receive_data("Project Configuration", request.form)
    return render_template("project_page.html")


if __name__ == "__main__":
    app.run()
