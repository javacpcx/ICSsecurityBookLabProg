from pyModbusTCP.client import ModbusClient
def run_plc_client():
    # 設置伺服器IP地址和端口
    address = '192.168.2.100'
    port = 502
    # 建置Modbus客户端
    client = ModbusClient(host=address, port=port)
    # 連接到伺服器
    if client.open():
        print(f"Connected to Modbus server at {address}:{port}")
        # 讀取保持暫存器的值
        holding_registers = client.read_holding_registers(0, 10)
        if holding_registers:
            print("Holding Registers:")
            for i, value in enumerate(holding_registers):
                print(f"Register {i}: {value}")
        else:
            print("Error reading holding registers.")
        # 讀取線圈的值
        coils = client.read_coils(0, 10)
        if coils:
            print("Coils:")
            for i, value in enumerate(coils):
                print(f"Coil {i}: {value}")
        else:
            print("Error reading coils.")
        # 寫入數值888到保持暫存器位址6
        write_register(client, 6, 888)
        # 寫入False到線圈位址0
        write_coil(client, 0, False)
        # 關閉連接
        client.close()
    else:
        print(f"Failed to connect to Modbus server at {address}:{port}")
def write_register(client, address, value):
    if client.write_single_register(address, value):
        print(
            f"Successfully written value {value} to holding register {address}.")
    else:
        print(f"Error writing value {value} to holding register {address}.")
def write_coil(client, address, value):
    if client.write_single_coil(address, value):
        print(f"Successfully written value {value} to coil {address}.")
    else:
        print(f"Error writing value {value} to coil {address}.")
if __name__ == '__main__':
    run_plc_client()