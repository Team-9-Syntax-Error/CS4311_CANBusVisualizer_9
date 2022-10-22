import cantools




class myclass():

    def __inti__(self):
        self.value = ""

    def run(self):
        db = cantools.db.load_file("/home/joseph/Workspace/software/CS4311_CANBusVisualizer_9/dbc_files/motohawk.dbc")

        import can 
        bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)

        while True:
            message = bus.recv(4)
            print(" I AM RECEIVINGNNG")
            print(db.decode_message(message.arbitration_id, message.data))
            self.value =  db.decode_message(message.arbitration_id, message.data)
            break
