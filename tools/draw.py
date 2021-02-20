import math
import numpy as np
import cv2

# palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)
sensitivity = 15
lower_red_0, upper_red_0 = np.array([0, 100, 100]), np.array([sensitivity, 255, 255])
lower_red_1, upper_red_1 = np.array([180 - sensitivity, 100, 100]), np.array([180, 255, 255])
lower_blue = np.array([120 - sensitivity, 100, 100])
upper_blue = np.array([120 + sensitivity, 255, 255])
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))


def compute_color_for_labels(img, point1, point2, label):
    """
    Simple function that detect car's color
    """
    car = img[point1[1]:point2[1], point1[0]:point2[0]]
    img_hsv = cv2.cvtColor(car, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)  # 获得蓝色部分掩膜
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)  # 闭运算
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)  # 开运算

    mask_0 = cv2.inRange(img_hsv, lower_red_0, upper_red_0)
    mask_1 = cv2.inRange(img_hsv, lower_red_1, upper_red_1)
    mask_red = cv2.bitwise_or(mask_0, mask_1)  # 获得红色部分掩膜
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)  # 闭运算
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)  # 开运算

    cnts1, hierarchy1 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测 红色
    cnts2, hierarchy2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 轮廓检测 蓝色
    if len(cnts1) < len(cnts2):
        color = (255, 0, 0)
    elif len(cnts1) > len(cnts2):
        color = (0, 0, 255)
    else:
        color = (255, 255, 255)
    return tuple(color)


def draw_boxes(img, bbox, angles, distance, tvec, identities=None, offset=(0, 0)):
    """

    Parameters
    ----------
    img  :原图
    bbox :目标框
    angles:偏转角度
    distance:距离
    tvec:三维坐标
    identities:编号
    offset:偏移量
    Returns
    -------
    """
    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(idx) for idx in box]
        angle = angles[i]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        HA = angle[0]
        VA = angle[1]
        # box text and bar
        id = int(identities[i]) if identities is not None else 0
        # 选目标的颜色
        color = compute_color_for_labels(img, (x1, y1), (x2, y2), id)
        label = '{}{:d}'.format("", id)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
        cv2.rectangle(img, (x1, y1), (x1 + t_size[0] + 3, y1 + t_size[1] + 4), color, -1)
        cv2.putText(img, label, (x1, y1 + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 2, [255, 255, 255], 2)
        # 打印相关信息
        HA_info = '{}{:.2f}'.format("HA : ", HA / 3.14 * 180)
        cv2.putText(img, HA_info
                    , (x2, y2 + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 1)

        VA_info = '{}{:.2f}'.format("VA : ", -VA / 3.14 * 180)
        cv2.putText(img, VA_info, (x2, y2 + t_size[1] * 2 + 8), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 1)

        Dist = '{}{:.2f}'.format("Dist : ", distance[i] / 1000)
        cv2.putText(img, Dist, (x2, y2 + t_size[1] * 3 + 12), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 1)

        # cur_point = [int(distance[i]*math.cos(VA)), int(distance[i]*math.cos(VA)*math.sin(HA))]
        # Posi =  '{}{:}'.format("Posi : ",cur_point)
        # cv2.putText(img, Posi, (x2, y2 + t_size[1]*4 + 16), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 2)

        # Tvec = np.array(tvec[i])
        # Posi = '{}{}'.format("3D : ", Tvec)
        # cv2.putText(img, Posi, (x2, y2 + t_size[1] * 4 + 16), cv2.FONT_HERSHEY_PLAIN, 1, [0, 255, 0], 2)
    return img


def draw_boxes(img, bbox, armor_color, identities=None, offset=(0, 0)):
    """

    Parameters
    ----------
    img  :原图
    bbox :目标框列表
    armor_color:装甲板颜色列表
    identities:编号
    offset:偏移量
    -------
    """
    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(idx) for idx in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        # box text and bar
        id = int(identities[i]) if identities is not None else 0
        # 选目标的颜色
        if armor_color[i] == 1: # RED
            color = (0,0,255)
        elif armor_color[i] == 2: # BLUE
            color = (255,0,0)
        else:
            color = (255,255,255)

        label = '{}{:d}'.format("", id)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
        cv2.rectangle(img, (x1, y1), (x1 + t_size[0] + 3, y1 + t_size[1] + 4), color, -1)
        cv2.putText(img, label, (x1, y1 + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 2, [255, 255, 255], 2)
    return img


if __name__ == '__main__':
    for i in range(82):
        print(compute_color_for_labels(i))
