import can
import cantools
import os
import json

class read_bus():

    def __init__(self):

        self.packet = None

        self.cwd = os.getcwd()
        self.db = cantools.db.load_file(self.cwd + "/dbc_files/motohawk.dbc") 
        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate = 250000)
        self.db_msg = self.db.get_message_by_name("ExampleMessage") # Gets message from DBC file

        self.json_data = []


    def receiveDBC(self):

        while True:
            message = self.bus.recv(4)
            print("Boooooom: ", message)
            print(" Reading:", self.bus.channel_info, " ...")
            if message:
                print("Decoded Message:", self.db.decode_message(message.arbitration_id, message.data))
                self.packet =  message

                if self.packet:                
                    self.writeJson()


    def writeJson(self, filename = "json_data.json"):
        with open(filename, "w", encoding = 'utf8') as f:
            self.packet = str(self.packet)
            tokens = self.packet.split()
            dl = " ".join(tokens[8:15])
            channel = tokens[17]
            annotate = '-'
            self.json_data.append({
                    "Timestamp": tokens[1],
                     "ID": tokens[3],
                     "S": tokens[5],
                     "DL": dl,
                     "Channel": channel,
                      "Annotate": annotate
              })
            json.dump(self.json_data, f, indent=4)
            print("JSON Created...")



