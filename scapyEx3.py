from scapy.all import *

# 定義要掃描的目標IP範圍
target_ip_range = "192.168.2.0/24"

# 指定使用的網卡介面名稱，例如 'eth0' 或 'wlan0'
interface = "乙太網路 2"

# 建立ARP請求封包，對所有IP位址進行廣播
arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip_range)

# 執行srp函式，使用指定的網卡介面，等待2秒鐘，並回傳收到的封包及沒有收到回應的封包
ans, unans = srp(arp_packet, iface=interface, timeout=2)

# 逐一處理收到的ARP回應封包
for sent_packet, received_packet in ans:
    # 從ARP回應封包中取得目標IP位址及MAC位址
    target_ip = received_packet[ARP].psrc
    target_mac = received_packet[Ether].src
    # 打印發現的目標設備的IP位址和MAC位址
    print("Found target device: IP=%s, MAC=%s" % (target_ip, target_mac))
