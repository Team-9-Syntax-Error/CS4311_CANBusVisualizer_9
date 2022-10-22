
from threading import Thread
from can_read import read_bus
from can_write import write_bus

def main():

    print("Ruinning t2")
    read = read_bus()
    thread2  = Thread(target = read.receiveDBC)
    thread2.start()

    print("Ruinning t1")
    writting = write_bus()
    writting.sendDBC()
    packet = read.value
    
    print("My message here:", packet)



main()
