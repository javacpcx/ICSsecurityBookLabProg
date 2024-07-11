import sys
from scapy.all import srp, Ether, ARP, conf, get_if_list

# 檢查命令行參數是否正確
if len(sys.argv) != 3:
    print("Usage: arping2tex <net> <interface>\n  eg: arping2tex 192.168.1.0/24 eth0")
    sys.exit(1)

# 取得命令行參數
net = sys.argv[1]
interface = sys.argv[2]

# 驗證網卡介面是否存在
if interface not in get_if_list():
    print(f"Interface {interface} does not exist. Available interfaces are: {get_if_list()}")
    sys.exit(1)

# 設定 Scapy
conf.verb = 0

# 發送 ARP 請求並等待回應
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=net), iface=interface, timeout=2)

# 輸出 LaTeX 表格的開頭
print(r"\begin{tabular}{|l|l|}")
print(r"\hline")
print(r"MAC & IP\\")
print(r"\hline")

# 處理每個收到的 ARP 回應封包
for snd, rcv in ans:
    print(rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\"))

# 輸出 LaTeX 表格的結尾
print(r"\hline")
print(r"\end{tabular}")
