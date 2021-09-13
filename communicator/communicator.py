import serial
import struct
import communicator.crc_table as crc_table
import communicator.rm_ui.RM_Client_UI as ui
import time
from color_conf import *


if FRIEND_COLOR == RED:
    SEND_BLUE = True
else:
    SEND_BLUE = False


def get_id(num):
        num = (num % 7) + 1
        if SEND_BLUE:
            return num + 100
        else:
            return num

class Communicator:
    """
    通信工具，用于与A板通信
    """
    # 定义包头和包尾
    head = 0xf1
    tail = 0xf2

    # 定义各功能的功能号
    MINIMAP = 0
    MOVING = 1

    PERIOD = .1 # 10Hz


    def __init__(self):
        self.error_code = 0
        try:
            self.communicator = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
        except serial.serialutil.SerialException:
            self.error_code = 1
            print("There is no usb")
        self.last_time = time.time()
        self.last_id = 0 # 0-based
    
    
    def cap_time(self):
        "Ensure not called more frequent than 10Hz"
        if time.time() - self.last_time > Communicator.PERIOD:
            return True
        else:
            return False
    
    def send_map(self, data: list):
        if not self.cap_time():
            return
        # time.sleep(0.1)
        if self.last_id >= data[0]:
            self.last_id = 0
        if data[0] == 0:
            return
        robot_id = get_id(self.last_id)
        x, y = data[1][self.last_id][0], data[1][self.last_id][1]

        buf = ui.create_string_buffer(256)
        ui.UI_SendMinimap305(buf, robot_id, 28 * x, 15 * (1-y))
        print("x, y: ", x, y)
        print(f"buf: {' '.join(map(hex, buf[:23]))}")
        self.communicator.write(buf[:9+14])
        self.last_id += 1
        

    def send(self, data_list: list, cmd: int) -> None:
        """
        功能：发送信息
        @param: data_list: 预先规定好的数据结构，以列表的形式保存
                cmd: 功能号
        """
        return self.send_map(data_list)

        sent_msg = "".encode()
        if cmd == self.MINIMAP:
            sent_msg = self.generate_minimap_sent_bytes(data_list)
        elif cmd == self.MOVING:
            sent_msg = self.generate_moving_sent_bytes(data_list)
        self.communicator.write(sent_msg)
        print("sent message: ", sent_msg)

    def generate_minimap_sent_bytes(self, data_list: list) -> bytes:
        """
        功能：生成发送小地图信息的数据流
        @param: data_list: 预先规定好的数据结构，以列表的形式保存
        return: 生成的数据流
        """
        tmp_list = [self.head, self.MINIMAP, data_list[0]]
        for i in range(len(data_list[1])):
            tmp_list.append(data_list[1][i][0])
            tmp_list.append(data_list[1][i][1])
        tmp_list.append(data_list[2])
        for i in range(len(data_list[3])):
            tmp_list.append(data_list[3][i][0])
            tmp_list.append(data_list[3][i][1])
        return self.generate_bytes(tmp_list)

    def generate_moving_sent_bytes(self, data_list: list) -> bytes:
        """
        功能：生成发送自动步兵移动位置信息的数据流
        @param: data_list: 预先规定好的数据结构，以列表的形式保存
        return: 生成的数据流
        """
        tmp_list = [self.head, self.MOVING, data_list[0], data_list[1]]
        return self.generate_bytes(tmp_list)

    def generate_bytes(self, tmp_list: list) -> bytes:
        """
        功能：根据所生成的列表转换成bytes
        @param: tmp_list: 包含所要转换成bytes流的所有数据
        """
        struct_format_str = "="
        for i in range(len(tmp_list)):
            struct_format_str += "B"
        tmp_bytes = struct.pack(struct_format_str, *tmp_list)
        data = self.compute_crc8(tmp_bytes)
        print("Command: ", tmp_list[1])
        print("bytes: ", tmp_bytes)
        print("crc8: ", data)
        remain_bytes = struct.pack("=BB", *[data, self.tail])
        tmp_bytes += remain_bytes
        return tmp_bytes

    def compute_crc8(self, data: bytes) -> bytes:
        """
        功能：计算所给bytes流的crc8校验码
        @param: bytes流
        """
        ucCRC8 = crc_table.CRC8_INIT
        for i in range(len(data)):
            ucIndex = ucCRC8 ^ data[i]
            ucCRC8 = crc_table.CRC8_Table[ucIndex]
        return ucCRC8

if __name__ == "__main__":
    data_list = [4, [[1, 3], [3, 4], [5, 6], [7, 8], [0, 0], [0, 0], [0, 0], [0, 0]],
                 4, [[1, 2], [3, 4], [5, 6], [7, 8], [0, 0], [0, 0], [0, 0], [0, 0]]]
    com = Communicator()
    com.send(data_list, com.MINIMAP)
