import numpy as np
import cv2

class Painter(object):
    """
    with this class Painter, you can display the image from zed camera and draw minimap and rectangles for cars
    """
    # camera window pos
    WINDOW_X = 690
    WINDOW_Y = 100
    # camera window size
    WINDOW_WIDTH = 1280
    WINDOW_HEIGHT = 720
    # size of map window
    MAP_WIDTH = 200
    MAP_LENGTH = 400

    # the classification of each car
    RED = 1
    BLUE = 2
    OTHERS = 3

    # current directory path
    cur_dir = '/home/radar/Desktop/go-radar-go/'

    def __init__(self):
        # minimap
        self.map_dir = self.cur_dir + 'pnp/map2019.png'

        self.map_src = cv2.imread(self.map_dir)  # (414, 765, 3)
        self.map_src = cv2.resize(self.map_src, (self.MAP_LENGTH, self.MAP_WIDTH))
        self.map_image = None

        self.map_x = 0
        self.map_y = 0

        self.map_auto_x = 0
        self.map_auto_y = 0

        self.left_mouse_down = False

        cv2.namedWindow('Zed_color', cv2.WINDOW_AUTOSIZE)
        # cv2.resizeWindow("Zed_color", WINDOW_WIDTH2, WINDOW_HEIGHT2)
        cv2.moveWindow("Zed_color", self.WINDOW_X, self.WINDOW_Y)

    # 在地图上绘制圆圈
    def paint_minimap(self, car_map_positions: list):
        """
        @func: paint minimap with circles of cars
        """
        self.map_image = self.map_src.copy()
        for pos in car_map_positions:
            if pos[2] == self.RED:
                color = (0, 0, 255)
            elif pos[2] == self.BLUE:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            cv2.circle(self.map_image, (int(pos[0]), int(pos[1])), 4, color, 6)

    def paint_color_image(self, car_rects: list, color_image: np.ndarray) -> np.ndarray:
        """
        @func: paint color image with the present color image and rectangles of cars
        """
        # draw rectangles
        for rect in car_rects:
            if rect.color_id == self.RED:
                color = (0, 0, 255)
            elif rect.color_id == self.BLUE:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            cv2.rectangle(color_image, (rect.left_top[0], rect.left_top[1]),
                          (rect.right_down[0], rect.right_down[1]), color, 3)
        return color_image

    def draw(self, car_map_positions: list, car_rects: list, color_image: np.ndarray):
        """
        @func: draw color image with rectangle of cars and minimap with circles of cars
        """
        # paint minimap and color image
        color_image = cv2.resize(color_image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.paint_minimap(car_map_positions)
        color_image = self.paint_color_image(car_rects, color_image)

        # Show images
        color_image[-self.MAP_WIDTH:, -self.MAP_LENGTH:, :] = self.map_image
        cv2.imshow('Zed_color', color_image)

        # Show Minimap
        # minimap = cv2.resize(self.map_image, (800, 400))
        # if self.left_mouse_down:
        #     cv2.circle(minimap, (int(self.map_auto_x), int(self.map_auto_y)), 4, (0, 255, 255), 6)
        # cv2.namedWindow('Map', cv2.WINDOW_AUTOSIZE)
        # # cv2.setMouseCallback('Map', self.map_on_mouse)
        # cv2.imshow('Map', minimap)
