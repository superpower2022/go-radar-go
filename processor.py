import numpy as np
from detect import DetectNet
from color_conf import *
import math


class Processor(object):
    """
    with this class Processor, you can process the information from zed camera.
    """
    # size of camera window (pixel)
    WIDTH = 1280
    HEIGHT = 720
    # size of map window (pixel)
    MAP_WIDTH = 200
    MAP_LENGTH = 400
    # size of real-world area (meter)
    AREA_WIDTH = 15
    AREA_LENGTH = 28

    ROBOTS_MAX_NUM = 8

    # cmd id
    MINIMAP = 0
    MOVING = 1

    # bias
    BIAS_X = 2150/1000/15*200

    def __init__(self):
        # detect net variables
        self.dnet = DetectNet()

        # rectangles of cars in RGB image
        self.car_rects = []

        # depth rectangles
        self.car_depth_rects = []

        # car depth positions
        self.car_depth_positions = []

        # car map positions
        self.car_map_positions = []

        # auto_car goto position
        self.auto_car_position = []

        self.outputs = []
        self.bbox_vxvy = []

        # list of message sent to A board
        self.message_positions = []

    def get_pack(self):
        """
        @func: pack the cars' position information to be sent to A board
        """
        friend_number = 0
        enemy_number = 0
        friend_position = []
        enemy_position = []
        self.message_positions.clear()

        # pack the cars' position information into a list
        for i in range(len(self.car_rects)):
            color_id = self.car_rects[i].color_id
            pos = [self.car_map_positions[i][0]/self.MAP_LENGTH, self.car_map_positions[i][1]/self.MAP_WIDTH]
            if color_id == FRIEND_COLOR:
                friend_number += 1
                friend_position.append(pos)
            else:
                enemy_number += 1
                enemy_position.append(pos)

        # if not all the cars are detected, the remained cars' position will be (0, 0)
        for i in range(self.ROBOTS_MAX_NUM - friend_number):
            friend_position.append([0, 0])

        for i in range(self.ROBOTS_MAX_NUM - enemy_number):
            enemy_position.append([0, 0])

        # packing
        # self.message_positions.append(friend_number)
        # self.message_positions.append(friend_position)
        self.message_positions.append(enemy_number)
        self.message_positions.append(enemy_position)

    # 将深度坐标 转为 地图坐标
    def trans_3d_to_map(self, world_coordinate: np.ndarray) -> (int, int):
        """
        @func: transform the 3D coordinate of cars into 2D coordinate on the map
        """
        map_x = round(self.MAP_WIDTH / 2 + world_coordinate[0] / self.AREA_WIDTH * self.MAP_WIDTH)
        map_y = round(self.MAP_LENGTH - (world_coordinate[2] / self.AREA_LENGTH * self.MAP_LENGTH))
        return map_x, map_y

    def processing(self, color_image: np.ndarray, point_cloud_image: np.ndarray) -> (list, list, list):
        """
        @func: process the information from camera, detect the cars' position
        and generate information list to be sent to A board
        return: three lists:
                1. car_map_positions: contain the positions of all detected cars
                2. message_positions: contain the information sent to A board
                3. car_rects: contain the rectangle information of all detected cars
        """
        # detect the cars with yolov5 net and generate the result of car positions
        self.dnet.detect(color_image)
        self.car_rects = self.dnet.car_rects

        # suppose the big rectangle is w * h, then the small rectangle with "*" is w/3 * h/6
        # |---------------------------------------------|
        # |                                             |
        # |                                             |
        # |                                             |
        # |                                             |
        # |                                             |
        # |                                             |
        # |                                             |
        # |---------------------------------------------|
        # |                                             |
        # |                                             |
        # |                                             |
        # |                     1/3                     |
        # |               ***************               |
        # |               *             *               |
        # |               *             *               |
        # |---------------***************---------------|

        # compute the distance of all the detected cars
        self.car_map_positions.clear()
        for car_rect in self.car_rects:
            left_top = car_rect.left_top
            right_down = car_rect.right_down
            sm_lt_x = (left_top[0] * 2 + right_down[0] * 1) // 3
            sm_lt_y = (right_down[1] + left_top[1]) // 2
            sm_rd_x = (left_top[0] * 1 + right_down[0] * 2) // 3
            sm_rd_y = (right_down[1] * 5 + left_top[1] * 1) // 6

            # get the small rectangle
            small_rect = point_cloud_image[sm_rd_y:right_down[1], sm_lt_x:sm_rd_x, :3]

            # change the array of shape (w/3, h/6, 3) into (w/3*h/6, 3)s
            small_rect = small_rect.reshape([(left_top[1]-right_down[1])//3*(right_down[0]-left_top[0])//3, 3])

            # compute the average coordinate
            world_coordinate = np.average(small_rect, axis=0)

            # print("x:", world_coordinate[0], " y:", world_coordinate[1], " z:", world_coordinate[2])
            try:
                map_x, map_y = self.trans_3d_to_map(world_coordinate)
                map_y *= math.cos(THETA / 180 * math.pi)
                if FRIEND_COLOR == RED:
                    self.car_map_positions.append([self.MAP_LENGTH - map_y, map_x - self.BIAS_X, car_rect.color_id])
                else:
                    self.car_map_positions.append([map_y, self.MAP_WIDTH - (map_x - self.BIAS_X), car_rect.color_id])
            except ValueError:
                pass

        # pack the cars' information to be sent to A board
        self.get_pack()

        return self.car_map_positions, self.message_positions, self.car_rects
