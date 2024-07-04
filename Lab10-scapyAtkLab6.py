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

    # 設定線圈地址和要寫入的值
    coil_addr = 0x0000
    coil_value = 0  # 0 表示 Off，1 表示 On

    # 寫入線圈值
    plc.execute(1, cst.WRITE_SINGLE_COIL, coil_addr, output_value=coil_value)
    print(f"已將線圈地址 {coil_addr} 的值設置為: {'Off' if coil_value == 0 else 'On'}")

    # 驗證線圈的值是否已經修改成功
    rr = plc.execute(1, cst.READ_COILS, coil_addr, 1)
    print(f"線圈地址 {coil_addr} 的修改後值: {'Off' if rr[0] == 0 else 'On'}")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    plc.close()
    print("PLC 連接已關閉")
