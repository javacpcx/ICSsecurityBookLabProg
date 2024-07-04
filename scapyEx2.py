from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

# 擷取網路封包，使用默認的網卡
sniff(prn=packet_callback, count=10)