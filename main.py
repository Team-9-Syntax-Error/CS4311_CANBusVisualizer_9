from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from data_handler import DataHandler
import os
import time
import can

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
    ("123456", "09/30/2022","Data Example 1" ),
)

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


# Create Project Page I made these comments for mysef so I dont get confused.- Victor Herrera
@app.route("/create_project")
def create_project():
    return render_template("Create_Project.html", date=today)


# Edit Configuration page
# When working on the project this will allow the user to modify the configuration
@app.route("/edit_config")
def edit_project():
    return render_template("edit_config.html", date=today)


@app.route("/project_page", methods=['POST', 'GET'])
def project_page():

    try:
        if request.method == 'POST':
            formName = request.form
            print(formName)
            if "start" in formName:
                PrintCan()
            if "stop" in formName:
                EndCan()
        return render_template("project_page.html", headings=headings, data=data)
    except:
        return render_template("project_page.html", headings=headings, data=data)


def PrintCan():
    id = 10
    bustype = 'socketcan'
    channel = 'vcan0'
    bus = can.Bus(channel=channel, interface=bustype)
    for i in range(10):
        msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
        bus.send(msg)
        print(msg)

def EndCan():
    print("Ending Can BUS.......")

if __name__ == "__main__":
    #Allows updates on page without running program over again. 
    app.run(debug=True)
