#!/usr/bin/env python3
"""
Modbus/TCP 服務器，只允許特定 IP 進行 Modbus 讀取和/或寫入操作。
"""
import argparse
import logging
from pyModbusTCP.server import ModbusServer, DataHandler
from pyModbusTCP.constants import EXP_ILLEGAL_FUNCTION
# 配置日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# some const
ALLOW_R_L = ['127.0.0.1', '192.168.0.10']
ALLOW_W_L = ['127.0.0.1']
# 自定義數據處理器，帶有 IP 過濾
class MyDataHandler(DataHandler):
    def read_coils(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            logger.info(f"Allowed read_coils from {srv_info.client.address}")
            return super().read_coils(address, count, srv_info)
        else:
            logger.warning(f"Blocked read_coils from {srv_info.client.address}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


    def read_d_inputs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            logger.info(f"Allowed read_d_inputs from {srv_info.client.address}")
            return super().read_d_inputs(address, count, srv_info)
        else:
            logger.warning(f"Blocked read_d_inputs from {srv_info.client.address}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


    def read_h_regs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            logger.info(f"Allowed read_h_regs from {srv_info.client.address}")
            return super().read_h_regs(address, count, srv_info)
        else:
            logger.warning(f"Blocked read_h_regs from {srv_info.client.address}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


    def read_i_regs(self, address, count, srv_info):
        if srv_info.client.address in ALLOW_R_L:
            logger.info(f"Allowed read_i_regs from {srv_info.client.address}")
            return super().read_i_regs(address, count, srv_info)
        else:
            logger.warning(f"Blocked read_i_regs from {srv_info.client.address}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


    def write_coils(self, address, bits_l, srv_info):
        if srv_info.client.address in ALLOW_W_L:
            logger.info(f"Allowed write_coils from {srv_info.client.address} with values: {bits_l}")
            return super().write_coils(address, bits_l, srv_info)
        else:
            logger.warning(f"Blocked write_coils from {srv_info.client.address} with attempted values: {bits_l}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


    def write_h_regs(self, address, words_l, srv_info):
        if srv_info.client.address in ALLOW_W_L:
            logger.info(f"Allowed write_h_regs from {srv_info.client.address} with values: {words_l}")
            return super().write_h_regs(address, words_l, srv_info)
        else:
            logger.warning(f"Blocked write_h_regs from {srv_info.client.address} with attempted values: {words_l}")
            return DataHandler.Return(exp_code=EXP_ILLEGAL_FUNCTION)


if __name__ == '__main__':
    # 解析參數
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='localhost', help='Host (default: localhost)')
    parser.add_argument('-p', '--port', type=int, default=502, help='TCP port (default: 502)')
    args = parser.parse_args()


    # 初始化 Modbus 服務器並啟動
    server = ModbusServer(host=args.host, port=args.port, data_hdl=MyDataHandler())
    logger.info(f"Starting Modbus server on {args.host}:{args.port}")
    server.start()