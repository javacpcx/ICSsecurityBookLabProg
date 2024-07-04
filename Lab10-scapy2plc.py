from scapy.all import *
import time
# 建置 Modbus/TCP 封包
def make_packet():
    pkt = Ether()/IP(dst="192.168.2.100")/TCP(dport=502)/Raw(load="\x00\x01\x00\x00\x00\x06\x01\x05\x00\x0F\x00\xFF")
    return pkt
# 發送 Modbus/TCP 封包
def send_packet(pkt):
    sendp(pkt, iface="eth0")
# 建置 Modbus/TCP 封包並發送
pkt = make_packet()
send_packet(pkt)
# 等待設備處理請求
time.sleep(1)
# 建置 Modbus/TCP 封包以將值設定為 0
pkt = make_packet()
pkt[Raw].load = "\x00\x01\x00\x00\x00\x06\x01\x05\x00\x0F\x00\x00"
send_packet(pkt)

