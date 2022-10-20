from wsgiref.util import request_uri
from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from data_handler import DataHandler
import can_rw
import json
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


"""
----------------- EVERYTHING UNDER HERE ARE SCRIPTS THAT MANIPULATE THE PAGES -------------------------

"""

# READS CAN BUS SCRIPT
@app.route("/project_page", methods=["GET", "POST"])
def project_page():
    print('Reading...')
    while True:
        packet = can_rw.read()
        if packet:
            packet = str(packet)
            tokens = packet.split()
            myvar = " ".join(tokens[8:])
            data.append([tokens[1], tokens[3], tokens[5], myvar])
            writeJson(data)
        return render_template("project_page.html", headings=headings, data=data)

def writeJson(data, filename="01_json_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        print("JSON Created...")


# WRITE TO CAN BUS SCRIPT
@app.route('/write')
def write():
    print('Writing...')
    can_rw.write()
    return render_template('project_page.html')


# Should access Json File of packets and edit Json file 
@app.route('/edit')
def edit():
    return render_template('project_page.html')

# 
@app.route('/annotate')
def annotate():
    return render_template('project_page.html')

# Should replay the saved packet json file
@app.route('/replay')
def replay():
    return render_template('project_page.html')

# Should save a json file of packets refer to print("My data: ", tokens[1], tokens[3], tokens[5], myvar) line of code
@app.route('/save')
def save():
    return render_template('project_page.html')

if __name__ == "__main__":
    #Allows updates on page without running program over again. 
    app.run(debug=True)
