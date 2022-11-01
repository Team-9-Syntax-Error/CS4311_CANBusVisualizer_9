# CS4311_CANBusVisualizer_9

sudo apt-get install can-utils;
sudo modprobe vcan;
sudo ip link add dev vcan0 type vcan;
sudo ip link set vcan0 up;
ip -details -statistics link show vcan0