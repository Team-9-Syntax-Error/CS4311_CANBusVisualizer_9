import cantools
import can
from can.message import Message



def run():
    db = cantools.db.load_file('/home/joseph/Workspace/software/CS4311_CANBusVisualizer_9/dbc_files/motohawk.dbc')

    msg = db.get_message_by_name('ExampleMessage')
    msg_data = msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    print(msg_data)
    msg = can.Message(arbitration_id=msg.frame_id, data=msg_data, is_extended_id=False)


    # Sending Msg here
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))

    except can.CanError:
        print("Message NOT sent")