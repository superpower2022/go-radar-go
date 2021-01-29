import serial
import struct
import time
import crc_table


def compute_crc8(data: bytes) -> bytes:
    ucCRC8 = crc_table.CRC8_INIT
    for i in range(len(data)):
        ucIndex = ucCRC8 ^ data[i]
        ucCRC8 = crc_table.CRC8_Table[ucIndex]
    return ucCRC8

def main():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
    if not ser.is_open:
        print("fail to open USB")
        exit(1)
    else:
        print("open USB successfully")
    while True:
        data_list = [0xf1, 0, 0, 100.0, 100.0, 1, 1]
        data = struct.pack("=BBBffBB", *data_list)
        tmp_list = [compute_crc8(data), 0xf2]
        data += struct.pack("=BB", *tmp_list)
        result = ser.write(data)
        print("written data length: ", result)
        time.sleep(1)


if __name__ == "__main__":
    main()
    # data_list = [0xf1, 0, 0, 100.0, 100.0, 1, 1]
    # data = struct.pack("=BBBffBB", *data_list)
    # tmp_list = [compute_crc8(data), 0xf2]
    # data += struct.pack("=BB", *tmp_list)
    # print(data)