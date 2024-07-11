from flask import Flask, render_template, jsonify
from pyModbusTCP.server import ModbusServer, DataBank
import threading
import time
import random

app = Flask(__name__)
server = ModbusServer(host="0.0.0.0", port=502, no_block=True)
bitList = [1, 0, 1, 0]

def modbus_server():
    try:
        server.start()
        print("Modbus TCP Server is running...")
        server.data_bank.set_coils(1, bitList)
        while True:
            for i in range(10):
                #server.data_bank.set_holding_registers(i, [i * 10])
                new_registers = [random.randint(0, 999) for _ in range(10)]                
                server.data_bank.set_holding_registers(0, new_registers)
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        server.stop()
    finally:
        server.stop()

@app.route('/')
def index():
    status = "Running" if server.is_run else "Stopped"
    return render_template('newIndex.html', status=status)

@app.route('/get_data')
def get_data():
    coils = server.data_bank.get_coils(1, 10)
    registers = server.data_bank.get_holding_registers(0, 10)
    return jsonify({
        'coils': coils,
        'registers': registers
    })

@app.route('/randomize_data')
def randomize_data():
    new_coils = [random.randint(0, 1) for _ in range(10)]
    new_registers = [random.randint(0, 999) for _ in range(10)]
    server.data_bank.set_coils(1, new_coils)
    server.data_bank.set_holding_registers(0, new_registers)
    return jsonify({
        'coils': new_coils,
        'registers': new_registers
    })

if __name__ == '__main__':
    modbus_thread = threading.Thread(target=modbus_server)
    modbus_thread.start()
    app.run(host='0.0.0.0', port=8080)
