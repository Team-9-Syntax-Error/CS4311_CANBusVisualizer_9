# CS4311_CANBusVisualizer_9

## Installing Dependencies
```bash
sudo apt-get install can-utils
sudo apt-get install python3-tk
pip install pyqt5
pip install pyqt5-tools
```

## Activating Can Utilties
```bash
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0
```


