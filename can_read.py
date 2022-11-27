import can
import cantools
import os
import json
from can_write import write_bus

class read_bus():

    def __init__(self):

        self.packet = None

        self.cwd = os.getcwd()
        self.db = cantools.db.load_file(self.cwd + "/dbc_files/comfort.dbc") 
        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate = 250000)
        #self.db_msg = self.db.get_message_by_name("ExampleMessage") # Gets message from DBC file

        self.json_data = {"packets" : []}
        self.decoded_json_data = []


    def receiveDBC(self):

        while True:
            message = self.bus.recv(4)
            print("Boooooom: ", message)
            print(" Reading:", self.bus.channel_info, " ...")
            if message:
                self.decoded = self.db.decode_message(message.arbitration_id, message.data)
                print("Decoded Message:", self.db.decode_message(message.arbitration_id, message.data))
                self.packet =  message

                if self.packet:                
                    self.writeJson()
                    self.writeDecodedJson()


    #The code below handles writing to JSON --> Decoded information and raw information

    def writeDecodedJson(self, filename = "decoded_data_json.json"):
        with open(filename, "w", encoding = 'utf8') as f:
            self.decoded = str(self.decoded)
            tokens = self.decoded.split()
            self.decoded_json_data.append({
                "Enable": tokens[1],
                "AverageRadius": tokens[3],
                "Temperature": tokens[5],
              })
            json.dump(self.decoded_json_data, f, indent=4)
            print("Decoded Json Created...")


    def writeJson(self, filename = "packet_data.json"):

        with open("Current_Working_Project.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    project_path = data["Project_path"]

        filename = project_path + "/"+ filename
        with open(filename, "w", encoding = 'utf8') as f:
            self.packet = str(self.packet)
            tokens = self.packet.split()
            dl = " ".join(tokens[8:15])
            channel = tokens[17]
            annotate = '-'
            self.json_data["packets"].append({
                    "timestamp": tokens[1],
                     "id": tokens[3],
                     "s": tokens[5],
                     "dl": dl,
                     "channel": channel,
                      "annotate": annotate
              })
            json.dump(self.json_data, f, indent=4)
            print("JSON Created...")



