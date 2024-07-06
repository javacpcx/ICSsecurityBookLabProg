from flask import Flask, render_template, redirect, url_for, request
from pyModbusTCP.server import ModbusServer, DataBank
import threading
import time

app = Flask(__name__)
server = ModbusServer(host="0.0.0.0", port=502, no_block=True)

def modbus_server():
    try:
        server.start()
        print("Modbus TCP Server is running...")
        while True:
            for i in range(10):
                DataBank.set_words(i, [i * 10])
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        server.stop()
    finally:
        server.stop()

@app.route('/', methods=['GET', 'POST'])
def index():
    if server.is_run:
        status = "Running"
    else:
        status = "Stopped"
    registers = DataBank.get_words(0, 10) or [0] * 10
    return render_template('newIndex.html', status=status, registers=registers, enumerate=enumerate)

@app.route('/update_registers', methods=['POST'])
def update_registers():
    for i in range(10):
        new_value = int(request.form[f'register_{i}'])
        DataBank.set_words(i, [new_value])
    return redirect(url_for('index'))

@app.route('/start')
def start_server():
    if not server.is_run:
        global modbus_thread
        modbus_thread = threading.Thread(target=modbus_server)
        modbus_thread.start()
    return redirect(url_for('index'))

@app.route('/stop')
def stop_server():
    if server.is_run:
        server.stop()
        global modbus_thread
        modbus_thread.join()
    return redirect(url_for('index'))

if __name__ == '__main__':
    modbus_thread = threading.Thread(target=modbus_server)
    modbus_thread.start()
    app.run(host='0.0.0.0', port=8080)
