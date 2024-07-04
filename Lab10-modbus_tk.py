import modbus_tk.defines as cst
from modbus_tk import modbus_tcp
# 設定 PLC 的 IP 和端口
PLC_IP = '192.168.2.100'
PLC_PORT = 502
try:
    # 連接到 PLC
    plc = modbus_tcp.TcpMaster(host=PLC_IP, port=PLC_PORT)
    plc.set_timeout(5.0)
    print(f"已成功連接到 PLC，IP: {PLC_IP}, 端口: {PLC_PORT}")
    # 讀取 PLC 的保持暫存器（Holding Register）的值
    addr = 0x0000
    nb = 1
    rr = plc.execute(1, cst.READ_HOLDING_REGISTERS, addr, nb)
    print(f"暫存器地址 {addr} 的原始值: {rr[0]}")
    # 修改暫存器的值
    wr = 12345
    plc.execute(1, cst.WRITE_SINGLE_REGISTER, addr, output_value=wr)
    print(f"已將暫存器地址 {addr} 的值修改為: {wr}")
    # 驗證暫存器的值是否已經修改成功
    rr = plc.execute(1, cst.READ_HOLDING_REGISTERS, addr, nb)
    print(f"暫存器地址 {addr} 的修改後值: {rr[0]}")
except Exception as e:
    print(f"發生錯誤: {e}")
finally:
    plc.close()
    print("PLC 連接已關閉")

