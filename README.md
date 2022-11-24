# CS4311_CANBusVisualizer_9

## Installing Dependencies
```bash
pip install python-can
pip install cantools
pip install flask
sudo apt-get install can-utils
sudo apt-get install python3-tk
pip install pyqt5
pip install pyqt5-tools
```
## Install JSON-Server
```bash
sudo apt install npm
sudo npm install -g json-server
npx json-server --watch packet_data.json --port 3000 //Start server JSON 
```
## Activating Can Utilties
```bash
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0
```

## Misc
Some of these installations are arbritrary depending on Kali Version
& PyQt5 specific installation fo reference
```base
pip install PyQt5==5.15.4
pip install markupsafe==2.0.1
```

