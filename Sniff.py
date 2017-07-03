#安装依赖包 pip install scapy-python3
from scapy.all import *
pcap = sniff(iface=conf.iface,count=50)
print(pcap)
print(conf.iface)
wrpcap('demo.pcap', pcap)
