import ctypes

# lib = ctypes.cdll.LoadLibrary("build/libRoboMasterUILib.so")

# print(lib.Line_Draw)

import RM_Client_UI as ui

def asArray(s: str):
    return (ui.c_char * 3)(*s.encode())

g = ui.Graph_Data()
ui.Circle_Draw(g, asArray("abc"), ui.UI_Graph_ADD, 0, ui.UI_Color_Yellow, 32, 500,500,100)

buf = ctypes.create_string_buffer(256)
# ui.UI_ReFresh(buf, 1, ui.byref(g))
# ui.UI_ReFresh(buf, 1, ui.byref(g))
ui.UI_SendMinimap305(buf, 1, 2., 3.)
# print(list(map(hex, buf.raw[:9+15+6])))
print(list(map(hex, buf.raw[:9+10])))

length = ui.UI_DrawCircle(buf)
print(list(map(hex, buf.raw[:length+1])))