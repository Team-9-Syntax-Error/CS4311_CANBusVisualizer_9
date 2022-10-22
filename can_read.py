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
            print(" Reading:", self.bus.channel_info, " ...")
            if message:
                print("Found Message:", self.db.decode_message(message.arbitration_id, message.data))
                self.packet =  message

                if self.packet:                
                    self.writeJson()
    

    def writeJson(self, filename = "json01_json_data.json"):
        with open(filename, "w", encoding = 'utf8') as f:
            
            self.packet = str(self.packet)
            tokens = self.packet.split()
            myvar = " ".join(tokens[8:])
            self.json_data.append({
                'Timestamp' : tokens[1],
                'ID' : tokens[3],
                 'S' : tokens[5],
                 'DL': myvar
              })
            json.dump(self.json_data, f, indent=4)
            print("JSON Created...")



