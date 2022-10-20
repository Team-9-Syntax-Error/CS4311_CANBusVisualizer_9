import cantools
from can.message import Message
db = cantools.db.load_file('/home/kevin/Documents/Test_2/motohawk.dbc')

#print particular message in dbc
msg = db.get_message_by_name('ExampleMessage')
msg_data = msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
print('DB HERE')
print(type(db))
print('DB HERE')

import can

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
msg = can.Message(arbitration_id=msg.frame_id, data=msg_data, is_extended_id=False)
try:
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))

except can.CanError:
    print("Message NOT sent")

"""

import cantools
from can.message import Message
db = cantools.db.load_file('/home/kevin/Documents/Test_2/comfort.dbc')

#print particular message in dbc
msg = db.get_message_by_name('VehicleMotion')
msg_data = msg.encode({'Velocity':4, 'CrashDetected': 1, 'EngineRunning': 1})

import can

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
msg = can.Message(arbitration_id=msg.frame_id, data=msg_data, is_extended_id=False)
try:
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))

except can.CanError:
    print("Message NOT sent")

"""