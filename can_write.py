import can
import cantools
import os
import random


class write_bus():

    def __init__(self):

        self.cwd = os.getcwd()
        self.db = cantools.db.load_file(self.cwd + "/dbc_files/comfort.dbc") 
        self.dbc_dictionary = {}
        self.db_set_up()
        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate = 250000)  
        self.db_msg = self.db.get_message_by_name("LockingRemoteControlRequest") # Gets message from DBC file

    def sendDBC(self):
        
        # Get single msg from db_dictionary:

        dictionary_list = list(self.dbc_dictionary.items())
        packet_name, info = random.choice(dictionary_list)
        print(packet_name)
        self.db_msg = self.db.get_message_by_name(packet_name) # Gets message from DBC file
        self.msg_data = self.db_msg.encode(info[0][0])
        self.msg = can.Message(arbitration_id=info[1][0], data=self.msg_data, is_extended_id=False)

        try:
            self.bus.send(self.msg)
            print("Message sent on {}".format(self.bus.channel_info), self.msg)

        except can.CanError:
            print("Message NOT sent")

    def db_set_up(self):

        self.sig_name = ""
        self.sig_unit = ""

        for msg in self.db.messages:
            self.msg_name = msg.name
            self.msg_id = msg.frame_id
            self.msg_length = msg.length
            self.sender = msg.senders
            self.msg_group = self.db.get_message_by_name(self.msg_name)

            signals = {}
            if len(self.msg_group.signals) != 0:
                for signal in self.msg_group.signals:
                    self.sig_name = signal.name
                    self.sig_start = signal.start
                    signals[self.sig_name] = self.sig_start

            self.dbc_dictionary[self.msg_name] = [[signals],[self.msg_id, self.msg_length, self.sender]]

