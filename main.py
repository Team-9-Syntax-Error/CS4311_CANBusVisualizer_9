from wsgiref.util import request_uri
from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from data_handler import DataHandler
import can_rw
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
@app.route("/", methods=["GET", "POST"])
def main_page():
    print("We are here123")
    if request.method == "POST":
        print("We are here")
        if "upload_folder" in request.form and request.form['upload_folder'] == "go":
            return render_template("project_page.html")
    else:
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


@app.route("/project_page")
def project_page():
    print('Reading...')

    while True:

        packet = can_rw.read()
        print(packet)
        if packet:
            packet = str(packet)
            tokens = packet.split()
            myvar = " ".join(tokens[8:])
            print("My data: ", tokens[1], tokens[3], tokens[5], myvar)
            data.append([tokens[1], tokens[3], tokens[5], myvar])
            print(data)
        return render_template("project_page.html", headings=headings, data=data)



@app.route('/write')
def write():
    print('Writing...')
    can_rw.write()
    return render_template('project_page.html')

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
