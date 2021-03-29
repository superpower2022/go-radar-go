import math

from cv2 import cv2 as cv
import numpy as np
from pnp.config import little_map as lm   #小地图的实例
'''
显示小地图流程：    1.调用get_rect_centerpoint(rects)取出中心点
                 2.调用show_little_map(points_2d)
'''
def get_red_armour(raw_frame,rects):
    '''
    从机器人目标检测中筛选出所有红色方机器人目标
    :param rects: rects[0]=x_center, rects[1]=y_center, rects[2]=width, rects[3]=height
           raw_frame: 摄像头拍摄的原图
    :return: red_armour: 红色机器人目标所在的rects
    '''
    #对原图处理 保留红色
    frame=cv.inRange(raw_frame,(0,0,140),(70, 70, 255))
    red_armour=[]
    threshold=10

    for rect in rects:
        account=0
        start_x=rect[0]-rects[2]/2
        end_x=rect[0]+rects[2]/2

        start_y=rect[1]-rects[3]/2
        end_y=rect[1]+rects[3]/2

        for x in range(start_x,end_x):
            for y in range(start_y,end_y):
                if frame[y][x]!=0:
                    account=account+1
                if account >=threshold:
                    red_armour.append(rect)
    return red_armour

def getArmorColor(raw_frame,rects):
    '''
    从机器人目标检测中筛选出所有蓝色方机器人目标
    :param rects: rects[0]=x_center, rects[1]=y_center, rects[2]=width, rects[3]=height
           raw_frame: 摄像头拍摄的原图
    :return: armour_color: 机器人目标对应list的颜色
    '''
    Red = 1
    Blue = 2
    Others = 3
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

    hsv = cv.cvtColor(raw_frame, cv.COLOR_BGR2HSV)
    #对原图处理 保留蓝色
    frame_blue = cv.inRange(hsv,(100, 43 , 46),(124, 255, 255))
    #对原图处理 保留红色
    frame_red1 = cv.inRange(hsv,(0,43,46),(10, 255, 255))
    frame_red2 = cv.inRange(hsv,(156,43,46),(180, 255, 255))
    frame_red = cv.bitwise_or(frame_red1, frame_red2)  # 获得融合的红色

    frame_blue = cv.morphologyEx(frame_blue, cv.MORPH_CLOSE, kernel)  # 闭运算
    frame_blue = cv.morphologyEx(frame_blue, cv.MORPH_OPEN, kernel)  # 开运算

    frame_red = cv.morphologyEx(frame_red, cv.MORPH_CLOSE, kernel)  # 闭运算
    frame_red = cv.morphologyEx(frame_red, cv.MORPH_OPEN, kernel)  # 开运算
    ''''''
    re = cv.resize(frame_red, (1280, 720))
    bl = cv.resize(frame_blue, (1280, 720))
    cv.imshow("red", re)
    cv.imshow("blue", bl)
    ''''''
    armor_color = []

    for rect in rects:
        start_x,start_y,end_x,end_y = [int(i) for i in rect]
        #  值得注意的是x和y的像素坐标是相反的
        red_rect = frame_red[start_y:end_y, start_x:end_x]
        blue_rect = frame_blue[start_y:end_y, start_x:end_x]

        # 通过对应颜色的轮廓数量判定
        cnts1, _ = cv.findContours(red_rect, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)  # 轮廓检测 红色
        cnts2, _ = cv.findContours(blue_rect, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)  # 轮廓检测 蓝色

        if len(cnts1) < len(cnts2):
            armor_color.append(Blue)
        elif len(cnts1) > len(cnts2):
            armor_color.append(Red)
        else:
            armor_color.append(Others)

    return armor_color
    
def getRectCenterpoint(rects):
    '''
    取矩形中心点
    :param rects: rects[0]=x_center, rects[1]=y_center, rects[2]=width, rects[3]=height
    :return: centerpoints: centerpoints[0]=x_center , centerpoints[1]=y_center
    '''
    centerpoints=[]
    # print("get_rect_centerpoint : ")
    for rect in rects:

        x1 = rect[0]
        y1 = rect[1]
        x2 = rect[2]
        y2 = rect[3]

        point = [int((x1+x2)/2), int((y1+y2)/2)]
        # print(point)
        centerpoints.append(point)

    # print(centerpoints)
    return centerpoints

def showLittleMap(lm,points_2d,motion,id,armor_color):
    '''
    显示小地图,并在地图上标记目标
    :param points_2d: 待标记的二维点坐标
    :return: None
    '''
    Red = 1
    Blue = 2
    Others = 3

    ratio = 0.5
    arrow_scale = 10
    cur_pic = lm.pic.copy()
    #基准点 即相机所在位置
    offset = (int(1/2 * lm.map_width), int(0.98 * lm.map_height))
    cv.circle(cur_pic, offset, 7, (0, 255, 0), 3)
    #小地图的缩放尺寸
    width = lm.get_width()*ratio
    height = lm.get_height()*ratio

    motion = np.array(motion)
    # print(width,height)
    #print("show_little_map : ")
    for i,point in enumerate(points_2d):
        # print("points_2d :",i," \n",points_2d)
        # print("motion : \n",motion[i])
        #当前运动趋势
        cur_motion = np.array(motion[i] *arrow_scale,dtype=np.int)
        #当前位置
        cur_position = (point[0], point[1])
        '''正常的投影变换 需要知道准确的相机高度与相机参数  ，所以先不用
                # scale_x = point[0]/(lm.count_width)*(lm.map_width)
                # scale_y = point[1]/(lm.count_height)*(lm.map_height)
                #
                # cur_position = (int( offset[0] + scale_x), int(offset[1]-scale_y))
                # print("scale : (",cur_position[0],",",cur_position[1],")")
                # print("point : (",point)
                # motion_direction = (point[0]+cur_motion[0] ,point[1]+cur_motion[1])
        '''
        #运动趋势
        motion_direction = (cur_position[0]+cur_motion[0] ,cur_position[1]+cur_motion[1])
        #打印牌号
        label = '{}{:d}'.format("", id[i])
        cv.putText(cur_pic,label,(cur_position[0]+10,cur_position[1]+10), cv.FONT_HERSHEY_PLAIN, 2, [255,255,255], 2)

        color = armor_color[i]
        if(color == Red):
            circle_color = (0, 0, 255)
        elif (color == Blue):
            circle_color = (255, 0, 0)
        else:
            circle_color = (255, 255, 255)
        #打印所在位置与运动趋势
        cv.circle(cur_pic, cur_position, 10,circle_color,2)
        cv.arrowedLine(cur_pic, cur_position, motion_direction, (0, 255, 0), 5, 8, 0, 0.3)

    cur_pic = cv.resize(cur_pic, (int(width), int(height)),interpolation=cv.INTER_AREA)

    return  cur_pic


def transform_3dpoints_to_2d(lm,tvec):
    '''
    影响因素多，待定

    将三维点转换成可显示在小地图上的二维点
    :param points_3d: 待转换的三维点坐标
    :return: points_2d
    '''
    points_2d = []
    Tvec = np.array(tvec)
    h = lm.radar_height
    for i in range(len(tvec)):
        # HA = angles[i][0]
        # VA = angles[i][1]
        # distance = dist[i]
        tvec_cur = Tvec[i]
        x = tvec_cur[0]
        y = -tvec_cur[1]
        z = tvec_cur[2]

        x_prime = x
        y_prime = math.sqrt(y*y+z*z-h*h)
        cur_point =[int(x_prime), int(y_prime)] # [int(tvec_cur[0]),-int(tvec_cur[1])]

        #cur_point = [int(distance*math.cos(VA)), int(distance*math.cos(VA)*math.sin(HA))]
        points_2d.append(cur_point)
    return points_2d

    # points_2d=[]
    # for point in points_3d:
    #
    #     points_2d.append(point)
    # return points_2d

# 测试用

#
# if __name__ == "__main__":
#
#
#
#
#