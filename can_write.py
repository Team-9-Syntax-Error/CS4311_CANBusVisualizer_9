import can
import cantools
import os

class write_bus():

    def __init__(self):
        self.cwd = os.getcwd()
        self.db = cantools.db.load_file(self.cwd + "/dbc_files/motohawk.dbc")

        self.bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate = 250000)
        self.db_msg = self.db.get_message_by_name("ExampleMessage") # Gets message from DBC file


    def sendDBC(self):
        self.msg_data = self.db_msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
        self.msg = can.Message(arbitration_id=self.db_msg.frame_id, data=self.msg_data, is_extended_id=False)

        try:
            self.bus.send(self.msg)
            print("Message sent on {}".format(self.bus.channel_info), self.msg)

        except can.CanError:
            print("Message NOT sent")



