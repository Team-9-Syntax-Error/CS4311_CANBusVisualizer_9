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

## Activating Can Utilties
```bash
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0
```

## Misc
Some of these installations are arbritrary depending on Kali Version

```base
pip install markupsafe==2.0.1
```

