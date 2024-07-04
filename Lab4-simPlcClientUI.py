from pyModbusTCP.client import ModbusClient
import requests
import time
import tkinter as tk
# 建立 Modbus 客户端
client = ModbusClient(host="127.0.0.1", port=502)
api_url = "http://127.0.0.1:8080/api/get_registers"
# 建置Tkinter界面
root = tk.Tk()
root.title("客戶端應用程式介面")
register_values = tk.StringVar()
label = tk.Label(root, textvariable=register_values, font=("Arial", 14))
label.pack(padx=10, pady=10)
def update_registers():
    while True:
        # 使用 Web API 從伺服器獲取保持暫存器的值
        response = requests.get(api_url)
        if response.status_code == 200:
            registers = response.json()
            register_values.set("保持暫存器的數值：{}".format(registers))
        else:
            register_values.set("獲取保持暫存器值失败")
        root.update()
        time.sleep(1)
update_registers()
root.mainloop()