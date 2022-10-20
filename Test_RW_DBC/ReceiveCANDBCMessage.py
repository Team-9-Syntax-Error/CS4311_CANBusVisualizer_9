from email import message
import cantools
from can.message import Message
db = cantools.db.load_file('/home/kevin/Documents/Test_2/motohawk.dbc')

import can 
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
while True:
    message = bus.recv()
    print(db.decode_message(message.arbitration_id, message.data))

"""

from email import message
import cantools
from can.message import Message
db = cantools.db.load_file('/home/kevin/Documents/Test_2/comfort.dbc')

import can 
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
while True:
    message = bus.recv()
    print(db.decode_message(message.arbitration_id, message.data))

"""