import can
import cantools
import os
import json
from can_write import write_bus
import ast


class read_bus(write_bus):

    def __init__(self):



        self.packet = None
        self.cwd = os.getcwd()
        self.db = cantools.db.load_file(self.cwd + "/dbc_files/comfort.dbc") 
        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate = 250000)
        #self.db_msg = self.db.get_message_by_name("ExampleMessage") # Gets message from DBC file
        self.json_data = {"packets" : []}
        self.decoded_json_data = []

        # Getting correcst DBC information form writer
        mywrite = write_bus()
        self.dbc_dictionary = mywrite.dbc_dictionary
        self.packet_name = mywrite.packet_name  
        self.info = mywrite.info
        self.msg_data = mywrite.msg_data
        #print(dictionary_list)
        self.blacklist = self.generate_blacklist()


    def generate_blacklist(self):
        
        blacklist = []
        with open("blacklist.txt", "r") as file:
            while (line := file.readline().rstrip()):
                blacklist.append(line)
        print(blacklist)
        return blacklist



    def receiveDBC(self):

        while True:
            message = self.bus.recv(4)
            print("Boooooom: ", message)
            print(" Reading:", self.bus.channel_info, " ...")
            if message and self.packet_name not in self.blacklist:
                self.decoded = self.db.decode_message(self.packet_name,  self.msg_data)
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
            self.decoded_json_data.append(ast.literal_eval(self.decoded))
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

            dl = ""
            myflag = True
            for i in range(8,len(tokens)):
                if myflag:
                    for char in tokens[i]:
                        if char == "C":
                            myflag = False
                            break
                        else:
                            dl+=str(char)
                else:
                    break
                
            
            channel = tokens[-1]
            annotate = '-'
            self.json_data["packets"].append({
                    "timestamp": tokens[1],
                     "id": tokens[3],
                     "s": tokens[5],
                     "dl": tokens[8],
                     "channel": channel,
                      "annotate": annotate
              })
            json.dump(self.json_data, f, indent=4)
            print("JSON Created...")



