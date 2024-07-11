import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from pyModbusTCP.client import ModbusClient

class ModbusClientApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = ModbusClient(host='127.0.0.1', port=502, unit_id=1)  # 默认UID为1
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Modbus Client')
        self.setGeometry(100, 100, 400, 500)  # 增加高度以容纳更多的元素

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.status_label = QLabel('Status: Disconnected', self)
        self.layout.addWidget(self.status_label)

        self.read_coils_button = QPushButton('Read Coils', self)
        self.read_coils_button.clicked.connect(self.read_coils)
        self.layout.addWidget(self.read_coils_button)

        self.coil_values = [QLineEdit(self) for _ in range(10)]
        for i, line_edit in enumerate(self.coil_values):
            line_edit.setPlaceholderText(f'Coil {i}')
            self.layout.addWidget(line_edit)

        self.read_registers_button = QPushButton('Read Registers', self)
        self.read_registers_button.clicked.connect(self.read_registers)
        self.layout.addWidget(self.read_registers_button)

        self.register_values = [QLineEdit(self) for _ in range(10)]
        for i, line_edit in enumerate(self.register_values):
            line_edit.setPlaceholderText(f'Register {i}')
            self.layout.addWidget(line_edit)

        self.connect_button = QPushButton('Connect', self)
        self.connect_button.clicked.connect(self.connect_server)
        self.layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton('Disconnect', self)
        self.disconnect_button.clicked.connect(self.disconnect_server)
        self.layout.addWidget(self.disconnect_button)

    def connect_server(self):
        if self.client.open():
            self.status_label.setText('Status: Connected')
        else:
            self.status_label.setText('Status: Connection Failed')

    def disconnect_server(self):
        self.client.close()
        self.status_label.setText('Status: Disconnected')

    def read_coils(self):
        if self.client.is_open:
            coils = self.client.read_coils(0, 10)
            if coils:
                for i in range(10):
                    self.coil_values[i].setText(str(coils[i]))
        else:
            self.status_label.setText('Status: Disconnected')

    def read_registers(self):
        if self.client.is_open:
            registers = self.client.read_holding_registers(0, 10)
            if registers:
                for i in range(10):
                    self.register_values[i].setText(str(registers[i]))
        else:
            self.status_label.setText('Status: Disconnected')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModbusClientApp()
    ex.show()
    sys.exit(app.exec_())
