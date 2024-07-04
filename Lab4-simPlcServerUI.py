from pyModbusTCP.server import DataBank, ModbusServer
from flask import Flask, request, jsonify, render_template_string
import threading
import time
app = Flask(__name__)
# 建立 Modbus 伺服器
server = ModbusServer("0.0.0.0", 502, no_block=True)
server.start()
# 設定初始數值
holding_registers = [0] * 10
# 更新保持暫存器的值
def update_registers():
    while True:
        DataBank.set_words(0, holding_registers)
        time.sleep(0.1)
# 啟動更新保持暫存器的執行緒
update_thread = threading.Thread(target=update_registers)
update_thread.start()
@app.route('/', methods=['GET'])
def index():
    return '''
    <h1>歡迎來到 Modbus 伺服器！</h1>
    <p><a href="/set_register_form">進入設定保持暫存器數值的表單</a></p>
    '''
@app.route('/set_register_form', methods=['GET', 'POST'])
def set_register_form():
    if request.method == 'POST':
        index = int(request.form['index'])
        value = int(request.form['value'])
        holding_registers[index] = value
        message = f"成功更新保持暫存器 {index} 的數值為 {value}"
    else:
        message = ""
    form_template = '''
    <h1>設定保持暫存器數值</h1>
    <form method="post">
        <label for="index">暫存器索引：</label>
        <input type="number" id="index" name="index" min="0" max="9" required>
        <br><br>
        <label for="value">數值：</label>
        <input type="number" id="value" name="value" required>
        <br><br>
        <input type="submit" value="提交">
    </form>
    <p>{{ message }}</p>
    <p><a href="/">返回首頁</a></p>
    '''
    return render_template_string(form_template, message=message)
@app.route('/api/get_registers', methods=['GET'])
def get_registers():
    return jsonify(holding_registers)
@app.route('/api/set_register', methods=['POST'])
def set_register():
    if request.is_json:
        data = request.get_json()
        if 'index' in data and 'value' in data:
            index = data['index']
            value = data['value']
            if 0 <= index < len(holding_registers):
                holding_registers[index] = value
                return jsonify({'result': 'success'})
            else:
                return jsonify({'result': 'error', 'message': 'Invalid index'})
        else:
            return jsonify({'result': 'error', 'message': 'Missing index or value'})
    else:
        return jsonify({'result': 'error', 'message': 'Invalid JSON'})
if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=8080)
    except KeyboardInterrupt:
        print("結束伺服器")
        server.stop()