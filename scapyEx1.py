from scapy.all import *

def send_icmp_packet(dst_ip):
    # 建置 ICMP 封包
    icmp_packet = IP(dst=dst_ip) / ICMP()
    
    # 發送封包並接收回應
    response = sr1(icmp_packet, timeout=1, verbose=0)
    
    if response:
        print(f"Received response from {dst_ip}: {response.summary()}")
    else:
        print(f"No response from {dst_ip}")

# 指定目標 IP 地址
target_ip = "8.8.8.8"
send_icmp_packet(target_ip)