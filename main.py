from lib2to3.pgen2 import token
from threading import Thread
from wsgiref.util import request_uri
from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from data_handler import DataHandler
import json
import os
from threading import Thread
from can_read import read_bus
from can_write import write_bus



app = Flask(__name__)

today = date.today()
today = today.strftime("%m/%d/%Y")
dh = DataHandler()

# Path 
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
json_folder_path = path + "/json"

#Project Page / Table information is comming
headings = ("Timestamp", "ID", "S", "DL")
data = []


# Classes for threads
read_class = read_bus()


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

# Open the Thread to Read on page Open
@app.route("/project_page", methods=["GET", "POST"])
def project_page():

    #Creating thread to open socket for reading..
    print("Ruinning Thread to recieve BUS")
    thread_read  = Thread(target = read_class.receiveDBC)
    thread_read.start()
        
    return render_template("project_page.html", headings=headings, data=data)


            
# WRITE TO CAN BUS SCRIPT
@app.route('/send')
def send():
    
    print('Sending packet...')
    writting = write_bus()
    writting.sendDBC()

    # Read packet from the reading Thread to update Table
    packet = None
    while not packet:
        packet = read_class.packet
    writeToTable(packet)
    

    return render_template('project_page.html', headings=headings, data=data)

def writeToTable(packet):
        if packet:
            packet = str(packet)
            tokens = packet.split()
            myvar = " ".join(tokens[8:])
            data.append([tokens[1], tokens[3], tokens[5], myvar])
            print("This is my data", data)
            #read_class.packet = None







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
