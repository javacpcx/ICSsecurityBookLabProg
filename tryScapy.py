from scapy.all import *
import struct
import time

def send_modbus_write_single_coil_request(dst_ip, coil_address, coil_value):
    # 1. 發送SYN
    syn = IP(dst=dst_ip) / TCP(dport=502, flags="S")
    syn_ack = sr1(syn, timeout=1, verbose=0)
    
    # 檢查回應是否為SYN-ACK
    if syn_ack and syn_ack.haslayer(TCP) and syn_ack[TCP].flags == "SA":
        # 2. 發送ACK
        ack = IP(dst=dst_ip) / TCP(dport=502, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags="A")
        send(ack, verbose=0)
        
        # 構造 Modbus 請求寫入線圈
        transaction_id = 1
        protocol_id = 0
        length = 6
        unit_id = 1
        function_code = 5  # Write Single Coil
        
        # 將 coil_address 和 coil_value 轉換為兩個字節的大端序
        modbus_payload = struct.pack('>HHHBBH', transaction_id, protocol_id, length, unit_id, function_code, coil_address)
        modbus_payload += struct.pack('>H', coil_value)
        
        # 構造 TCP/IP 封包
        req = IP(dst=dst_ip) / TCP(dport=502, sport=syn_ack[TCP].dport, seq=ack.seq, ack=ack.ack, flags="PA") / Raw(load=modbus_payload)
        
        # 持續發送封包直到接收到回應
        response = sr1(req, timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags == "PA":
            print("Received Modbus response:", response.summary())
        else:
            print("No response received.")
        
        # 傳送 FIN 封包終止連接
        fin = IP(dst=dst_ip) / TCP(dport=502, sport=syn_ack[TCP].dport, seq=ack.seq + len(modbus_payload), ack=ack.ack, flags="FA")
        fin_ack = sr1(fin, timeout=1, verbose=0)
        
        if fin_ack and fin_ack.haslayer(TCP) and fin_ack[TCP].flags == "FA":
            print("Connection closed successfully.")
        else:
            print("Failed to close connection.")
    else:
        print("Failed to establish connection.")

# 發送 Modbus/TCP 請求到指定IP地址，寫入線圈 0x0000 為 0 (Off)
send_modbus_write_single_coil_request("192.168.2.3", 0x0000, 0x0000)
