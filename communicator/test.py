import serial
import struct
import time
import crc_table
import rm_ui.RM_Client_UI as ui


def compute_crc8(data: bytes) -> bytes:
    ucCRC8 = crc_table.CRC8_INIT
    for i in range(len(data)):
        ucIndex = ucCRC8 ^ data[i]
        ucCRC8 = crc_table.CRC8_Table[ucIndex]
    return ucCRC8


def asArray(s: str):
    return (ui.c_char * 3)(*s.encode())


def receive(ser: serial.Serial):
    cnt = 0
    while True:
        cnt += 1
        sof = ser.read(1)[0]
        if sof == 0xa5:
            break
    d = ser.read(2)
    length = d[0] + 256 * d[1]
    seq, crc = ser.read(2)

    return [sof, *d, seq, crc, ser.read(length+4)]
    # return ser.read(256)


def main():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
    if not ser.is_open:
        print("fail to open USB")
        exit(1)
    else:
        print("open USB successfully")
    while True:
        # g = ui.Graph_Data()
        # ui.Circle_Draw(g, asArray("cir"), ui.UI_Graph_ADD, 0, ui.UI_Color_Yellow, 32, 500, 500, 100)
        buf = ui.create_string_buffer(256)
        # ui.UI_ReFresh(buf, 1, ui.byref(g))
        # data = buf[0:9+9+15+10]

        # ui.UI_DrawFloat(buf, asArray("flt"), ui.UI_Graph_ADD, 1, ui.UI_Color_Black, 20, 3, 20, 200, 300, 1.5)
        # data = buf[:9+6+15]
        # print(f"Written data: {' '.join(map(hex, data))}")
        # ser.write(data)
        
        ui.UI_SendMinimap305(buf, ui.UI_Data_RobotID_BStandard2, 12, 10)
        data = buf[0:9+14]
        print(f"Written data: {' '.join(map(hex, data))}")
        ser.write(data)

        # buflen = ui.UI_DrawCircle(buf, ui.UI_Graph_ADD, 6, ui.UI_Color_Green, 10, 1600, 800, 1700, 100)
        # data = buf[:buflen]
        # print(f"Written data: {' '.join(map(hex, data))}")
        # ser.write(data)

        time.sleep(0.10)

        ui.UI_SendMinimap305(buf, ui.UI_Data_RobotID_BStandard1, 21, 14)
        data = buf[0:9+14]
        print(f"Written data: {' '.join(map(hex, data))}")
        ser.write(data)

        ui.send_multi_graphic(buf)
        data = buf[:9+6+15*7]
        print(f"Written data: {' '.join(map(hex, data))}")
        # print(data)
        ser.write(data)



        # ui.referee_send_map(buf, ui.UI_Data_RobotID_BAerial, 5, 3)
        # data = buf[:19]
        # print(f"Written data: {' '.join(map(hex, data))}")
        # ser.write(data)


        # data_list = [0xf1, 0, 0, 100.0, 100.0, 100., 1, 1]
        # data = struct.pack("=BBBfffBB", *data_list)
        # data += struct.pack("=Hff", 0x105, 12., 13.)
        # tmp_list = [compute_crc8(data), 0xf2]
        # data += struct.pack("=BB", *tmp_list)
        # result = ser.write(data)
        # print("written data length: ", result)
        # print(f"Written data: {data}")

        # data = struct.pack("<Hff", ui.UI_Data_CilentID_RStandard1, 2., 3.)
        # header = struct.pack("<BHB", 0xa5, 10, 1)
        # header = bytes(*header, compute_crc8(header))
        # cmd_id = 0x305
        # print(data)
        time.sleep(.5)
        print("Received", receive(ser))


if __name__ == "__main__":
    main()
    # data_list = [0xf1, 0, 0, 100.0, 100.0, 1, 1]
    # data = struct.pack("=BBBffBB", *data_list)
    # tmp_list = [compute_crc8(data), 0xf2]
    # data += struct.pack("=BB", *tmp_list)
    # print(data)
