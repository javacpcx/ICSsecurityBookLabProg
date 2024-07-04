from pyModbusTCP.client import ModbusClient
def run_plc_client():
    # 設定服務位址和埠
    address = 'localhost'
    port = 502
    # 建置Modbus客户端
    client = ModbusClient(host=address, port=port)
    # 連接到伺服器
    if client.open():
        print(f"Connected to Modbus server at {address}:{port}")
        # 讀取保持暫存器的值
        holding_registers = client.read_holding_registers(0, 16)
        if holding_registers:
            print("Holding Registers:")
            for i, value in enumerate(holding_registers):
                print(f"Register {i}: {value}")
        else:
            print("Error reading holding registers.")
        # 讀取線圈的值
        coils = client.read_coils(0, 16)
        if coils:
            print("Coils:")
            for i, value in enumerate(coils):
                print(f"Coil {i}: {value}")
        else:
            print("Error reading coils.")
        # 關閉連接
        client.close()
    else:
        print(f"Failed to connect to Modbus server at {address}:{port}")
if __name__ == '__main__':
    run_plc_client()