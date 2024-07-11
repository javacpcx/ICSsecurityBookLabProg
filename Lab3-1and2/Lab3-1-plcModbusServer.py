from pyModbusTCP.server import ModbusServer, DataBank
def run_plc_simulator():
    # 設定IP地址和埠
    address = 'localhost'
    port = 502
    wordList=[999,888,777]
    bitList=[1,0,1,0]
    # 建置Modbus TCP服務
    server = ModbusServer(address, port, no_block=True)
    # 設定數據存儲的初始值
    # Write data to server input registers space
    server.data_bank.set_input_registers(1, [666])
    #Write data to server holding registers space
    server.data_bank.set_holding_registers(1, wordList)
    #Write data to server coils space
    server.data_bank.set_coils(1, bitList)
    #Write data to server discrete inputs space
    server.data_bank.set_discrete_inputs(5,[True])
    try:
        # 啟動Modbus TCP伺服器
        print(f"Starting Modbus TCP server at {address}:{port}")
        server.start()
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop()
if __name__ == '__main__':
    run_plc_simulator()