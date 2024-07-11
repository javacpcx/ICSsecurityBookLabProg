# app.py
from flask import Flask, render_template
from pyModbusTCP.server import ModbusServer, DataBank
import threading
import time
#import random
app = Flask(__name__)
server = ModbusServer(host="0.0.0.0", port=502, no_block=True)
#wordList=[999,888,777]
bitList=[1,0,1,0]
def modbus_server():
    try:
        server.start()
        print("Modbus TCP Server is running...")
        #server.data_bank.set_input_registers(1, [666])
        #Write data to server holding registers space
        #server.data_bank.set_holding_registers(1, wordList)
        #Write data to server coils space
        server.data_bank.set_coils(1, bitList)
        # #Write data to server discrete inputs space
        #server.data_bank.set_discrete_inputs(5,[True])        
        #server.data_bank.set_input_registers(8, random.randint(0, 999))
        while True:
            for i in range(10):                                
                server.data_bank.set_holding_registers(i, [i * 10])
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        server.stop()
    finally:
        server.stop()
@app.route('/')
def index():
    if server.is_run:
        status = "Running"
    else:
        status = "Stopped"
    return render_template('index.html', status=status)
if __name__ == '__main__':
    modbus_thread = threading.Thread(target=modbus_server)
    modbus_thread.start()
    app.run(host='0.0.0.0', port=8080)