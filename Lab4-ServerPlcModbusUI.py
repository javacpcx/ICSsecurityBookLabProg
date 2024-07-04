# app.py
from flask import Flask, render_template
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