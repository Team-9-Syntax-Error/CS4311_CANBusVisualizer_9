
import can

bus = can.Bus(channel='vcan0', interface='socketcan')

def read():

    message = bus.recv(1.0)
    if message is None:
        print("Reading ... ")
        return None
    else:
        print("Reading: ", message)
        return message


def write():

    for i in range(10):
        msg = can.Message(arbitration_id=0xc0ffee, data=[10, i, 0, 1, 3, 1, 4, 1], is_extended_id=False)
        bus.send_periodic(msg, 1)
    print("Finished Writing")


# Copy paste this into terminal to test virtual can
"""
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0

"""
