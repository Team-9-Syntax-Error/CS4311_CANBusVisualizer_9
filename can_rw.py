import can
import cantools
import os

cwd = os.getcwd()
db = cantools.db.load_file(cwd + "/dbc_files/motohawk.dbc")

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

def receiveDBC():
    message = bus.recv()
    if message is None:
        print("None ... ")
        return None
    else:
        print(message)
        return message


def sendDBC():
    msg_data = msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
    msg = can.Message(arbitration_id=msg.frame_id, data=msg_data, is_extended_id=False)
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))

    except can.CanError:
        print("Message NOT sent")

# Copy paste this into terminal to test virtual can
"""
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0

"""
