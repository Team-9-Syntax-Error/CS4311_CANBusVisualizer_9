from wsgiref.util import request_uri
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
headings = ("Timestamp", "ID", "S", "DL")
data = []

# This is our Main Page / First Page that appears
@app.route("/")
def main_page():
    return render_template("main_page.html")

# Path of where to save
app.config["UPLOAD_FILES"] = "/GitHub/CS4311_CANBusVisualizer_9/static/img/uploads/"


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            files = request.files['Upload'] # Access with the tag name 'Upload' that was setup in html
            print(files)
        return redirect(request.url)
    return render_template("upload_file.html")


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
    if request.method == 'POST':
        myfrom = request.form
        if "submit_button" in request.form and request.form['submit_button'] == "Stop":
            return render_template("project_page.html", headings=headings, data=[])

        elif "submit_button" in request.form and request.form['submit_button'] == "Start":
            mydata = PrintCan()
            for packet in mydata:
                tokens = packet.split()
                myvar = " ".join(tokens[8:])
                data.append([tokens[1], tokens[3], tokens[5], myvar])
            return render_template("project_page.html", headings=headings, data=data)
        return render_template("project_page.html", headings=headings, data=[])
    return render_template("project_page.html", headings=headings, data=[])


def saveData():
    pass

def PrintCan():
    id = 10
    bustype = 'socketcan'
    channel = 'vcan0'
    bus = can.Bus(channel=channel, interface=bustype)
    thisdata = []
    for i in range(10):
        msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
        bus.send(msg)
        thisdata.append(str(msg))

    return thisdata

def EndCan():
    print("Ending Can BUS.......")

if __name__ == "__main__":
    #Allows updates on page without running program over again. 
    app.run(debug=True)
