import cantools
import can
from can.message import Message



def run():
    db = cantools.db.load_file('/home/joseph/Workspace/software/CS4311_CANBusVisualizer_9/dbc_files/motohawk.dbc')

    for msg in db.messages:
        msg_name = msg.name
        msg_id = msg.frame_id
        msg_length = msg.length
        sender = msg.senders
        msg_group = db.get_message_by_name(msg_name)

    for signal in msg_group.signals:
            #name of signal
            sig_name = signal.name
            #unit of signal
            sig_unit = signal.unit
    
    print("Unit: ", sig_name)
    print("Unit", sig_unit)

    #msg = db.get_message_by_name('ExampleMessage')



    msg_data = msg.encode({'Enable':1, 'AverageRadius': 1, 'Temperature': 251})
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    print(msg_data)
    msg = can.Message(arbitration_id=msg_id, data=msg_data, is_extended_id=False)


    # Sending Msg here
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))

    except can.CanError:
        print("Message NOT sent")

'''
 #**dbc_file** is the full path of dbc 
    db = cantools.database.load_file(dbc_file)
    for msg in db.messages:
        msg_name = msg.name
        msg_id = msg.frame_id
        msg_length = msg.length
        sender = msg.senders
        msg_group = db.get_message_by_name(msg_name)
    
        for signal in msg_group.signals:
            
            #name of signal
            sig_name = signal.name
            #unit of signal
            sig_unit = signal.unit
'''