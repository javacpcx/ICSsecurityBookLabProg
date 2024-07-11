import tkinter as tk
from pyModbusTCP.client import ModbusClient
import threading
import time

class CustomModbusClient(ModbusClient):
    def open(self):
        return super().open()

# 建置Modbus客户端
client = CustomModbusClient(auto_open=True)
connection_status = "Disconnected"

def update_connection_status():
    while True:
        connection_status_label.config(text=connection_status)
        time.sleep(1)

def read_registers():
    global connection_status
    while True:
        if client.is_open:
            connection_status = "Connected"
            try:
                registers = client.read_holding_registers(0, 10)
                coils = client.read_coils(0, 10)
                if registers:
                    for i, value in enumerate(registers):
                        register_entries[i].delete(0, tk.END)
                        register_entries[i].insert(0, value)
                if coils:
                    for i, value in enumerate(coils):
                        coil_entries[i].delete(0, tk.END)
                        coil_entries[i].insert(0, value)
            except Exception as e:
                print(f"Error: {e}")
        else:
            connection_status = "Disconnected"
        time.sleep(1)

def write_register(index):
    try:
        value = int(register_entries[index].get())
        client.write_single_register(index, value)
    except Exception as e:
        print(f"Error: {e}")

def write_coil(index):
    try:
        value = int(coil_entries[index].get())
        client.write_single_coil(index, bool(value))
    except Exception as e:
        print(f"Error: {e}")

def connect():
    global connection_status
    host = host_entry.get()
    port = int(port_entry.get())
    client.host = host
    client.port = port
    client.open()

root = tk.Tk()
root.title("Modbus TCP Client")

host_label = tk.Label(root, text="Host:")
host_label.grid(row=0, column=0)
host_entry = tk.Entry(root, width=20)
host_entry.grid(row=0, column=1)

port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0)
port_entry = tk.Entry(root, width=20)
port_entry.grid(row=1, column=1)

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.grid(row=2, column=1)

connection_status_label = tk.Label(root, text=connection_status)
connection_status_label.grid(row=3, column=1)

# Holding Registers
tk.Label(root, text="Holding Registers").grid(row=4, column=0, columnspan=2)
register_entries = [tk.Entry(root, width=10) for _ in range(10)]
for i, entry in enumerate(register_entries):
    entry.grid(row=i + 5, column=0)
register_buttons = [tk.Button(root, text="Write", command=lambda index=i: write_register(index)) for i in range(10)]
for i, button in enumerate(register_buttons):
    button.grid(row=i + 5, column=1)

# Coils
tk.Label(root, text="Coils").grid(row=15, column=0, columnspan=2)
coil_entries = [tk.Entry(root, width=10) for _ in range(10)]
for i, entry in enumerate(coil_entries):
    entry.grid(row=i + 16, column=0)
coil_buttons = [tk.Button(root, text="Write", command=lambda index=i: write_coil(index)) for i in range(10)]
for i, button in enumerate(coil_buttons):
    button.grid(row=i + 16, column=1)

read_thread = threading.Thread(target=read_registers, daemon=True)
read_thread.start()
status_thread = threading.Thread(target=update_connection_status, daemon=True)
status_thread.start()

root.mainloop()
