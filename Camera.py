import pyzed.sl as sl
import numpy as np
import cv2
from detect import DetectNet, CarRect
from communicator import communicator


class Camera:
    # size of camera window
    WIDTH = 1280
    HEIGHT = 720
    # size of map window
    MAP_WIDTH = 200
    MAP_LENGTH = 400
    # size of actural area
    AREA_WIDTH = 10
    AREA_LENGTH = 20

    RED = 1
    BLUE = 2
    OTHERS = 3

    # friend color
    FRIEND_COLOR = BLUE

    ROBOTS_MAX_NUM = 8

    # cmd id
    MINIMAP = 0
    MOVING = 1

    cur_dir = '/home/radar/Desktop/go-radar-go/'

    def __init__(self):
        # Create a Camera object
        self.zed = sl.Camera()

        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE  # Use PERFORMANCE depth mode
        init_params.coordinate_units = sl.UNIT.METER  # Use meter units (for depth measurements)
        init_params.camera_resolution = sl.RESOLUTION.HD720

        # Open the camera
        err = self.zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(1)

        # Create and set RuntimeParameters after opening the camera
        self.runtime_parameters = sl.RuntimeParameters()
        self.runtime_parameters.sensing_mode = sl.SENSING_MODE.STANDARD  # Use STANDARD sensing mode
        # Setting the depth confidence parameters
        self.runtime_parameters.confidence_threshold = 100
        self.runtime_parameters.textureness_confidence_threshold = 100

        # present frame data
        self.image_frame = sl.Mat()

        # present depth frame data
        self.depth_frame = sl.Mat()

        # present color frame data
        self.point_cloud = sl.Mat()

        # present color numpy array
        self.color_image = None

        # present depth numpy array
        self.depth_image = None

        # The present xyz of the point
        self.world_coordinate = None

        # present mouse position
        self.X = self.WIDTH // 2
        self.Y = self.HEIGHT // 2

        # present distance
        self.dist = 0.0

        # residual frames count
        self.residual_frame_count = 100

        # detected number
        self.detected_number = 3

        # points residual
        self.points_res = [[] for i in range(self.detected_number)]

        # present objects position
        self.pre_obj_position = [[] for i in range(self.detected_number)]

        # tmp position data
        self.tmp_position_data = None

        #---------------------------------------------------------------------
        # detect net
        self.dnet = DetectNet()

        # rects of cars in RGB image
        self.car_rects = []

        # depth rects
        self.car_depth_rects = []

        # car depth positions
        self.car_depth_positions = []

        # car map positions
        self.car_map_positions = []

        # auto_car goto position
        self.auto_car_position = []

        self.outputs = []
        self.bbox_vxvy = []
        self.car_rects = []

        #----------------------------------------------------------------
        # little map
        # 标定小地图
        self.map_dir = self.cur_dir + 'pnp/map2019.png'

        self.map_image = cv2.imread(self.map_dir)       # (414, 765, 3)
        self.map_image = cv2.resize(self.map_image, (self.MAP_LENGTH, self.MAP_WIDTH))
        self.map_src = self.map_image.copy()

        self.map_x = 0
        self.map_y = 0

        self.map_auto_x = 0
        self.map_auto_y = 0

        self.left_mouse_down = False
        # ----------------------------------------------------------------
        # communicator
        try:
            self.communicator = communicator.Communicator()
        except:
            pass

        # message to send
        self.message_positions = []
        self.message_auto_pos = []

    def get_camera_xyz(self):
        err, self.world_coordinate = self.point_cloud.get_value(self.X, self.Y)
        print("x:", self.world_coordinate[0], " y:", self.world_coordinate[1], " z:", self.world_coordinate[2])

    # 将深度坐标 转为 地图坐标
    def trans_3d_to_map(self):
        self.map_x = round(self.MAP_WIDTH / 2 + self.world_coordinate[0] / self.AREA_WIDTH * self.MAP_WIDTH)
        self.map_y = round(self.MAP_LENGTH - (self.world_coordinate[2] / self.AREA_LENGTH * self.MAP_LENGTH))

    # 传入相机坐标系x和z轴的坐标
    def trans_depth_to_map(self, x, z):
        self.map_x = round(self.MAP_WIDTH/2 + x / self.AREA_WIDTH * self.MAP_WIDTH)
        self.map_y = round(self.MAP_LENGTH - (z / self.AREA_LENGTH * self.MAP_LENGTH))
        return [self.map_x, self.map_y]

    # 鼠标回调函数，用于选择自动步兵移动位置，通信时去注释
    def map_on_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.map_auto_x = x
            self.map_auto_y = y
            self.message_auto_pos = [self.map_auto_x // 2, self.map_auto_y // 2]
            # 与A板通信时使用
            # self.SendToAutoCar()
            self.left_mouse_down = True

    # 在地图上绘制圆圈
    def get_map(self):
        for pos in self.car_map_positions:
            if pos[2] == self.RED:
                color = (0, 0, 255)
            elif pos[2] == self.BLUE:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            cv2.circle(self.map_image, (int(pos[0]), int(pos[1])), 4, color, 6)

    # yolov5 识别车辆，返回矩阵信息
    def GetCarRects(self):
        self.dnet.detect(self.color_image)
        self.car_rects = self.dnet.car_rects

        # draw rectangles
        for rect in self.car_rects:
            if rect.color_id == self.RED:
                color = (0, 0, 255)
            elif rect.color_id == self.BLUE:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)
            cv2.rectangle(self.color_image, (rect.left_top[0], rect.left_top[1]),
                          (rect.right_down[0], rect.right_down[1]), color, 3)

    # 截取矩阵对应的深度矩阵
    def GetRectDepths(self):
        pass

    # 根据深度计算装甲车的位置
    def GetPos(self):
        for car_rect in self.car_rects:
            left_top = car_rect.left_top
            right_down = car_rect.right_down
            ########################################
            center_point = (left_top + right_down) / 2
            err, self.world_coordinate = self.point_cloud.get_value(int(center_point[0]), int(center_point[1]))
            try:
                self.trans_3d_to_map()
                self.car_map_positions.append([self.MAP_LENGTH - self.map_y, self.map_x, car_rect.color_id])
            except ValueError:
                pass

    # 将装甲车位置信息打包
    def GetPack(self):
        friendNumber = 0
        enemyNumber = 0
        friendPosition = []
        enemyPosition = []
        self.message_positions = []
        for i in range(len(self.car_rects)):
            color_id = self.car_rects[i].color_id
            pos = [self.car_map_positions[0], self.car_map_positions[1]]
            if color_id == self.FRIEND_COLOR:
                friendNumber += 1
                friendPosition.append(pos)
            else:
                enemyNumber += 1
                enemyPosition.append(pos)

        for i in range(self.ROBOTS_MAX_NUM - friendNumber):
            friendPosition.append([0, 0])

        for i in range(self.ROBOTS_MAX_NUM - enemyNumber):
            enemyPosition.append([0, 0])

        # 打包
        self.message_positions.append(friendNumber)
        self.message_positions.append(friendPosition)
        self.message_positions.append(enemyNumber)
        self.message_positions.append(enemyPosition)

    # 将小地图位置信息发送给所有客户端
    def SendToAll(self):
        self.communicator.send(self.message_positions, self.MINIMAP)

    # 将移动位置发送给自动步兵
    def SendToAutoCar(self):
        self.communicator.send(self.message_auto_pos, self.MOVING)

    # 一帧的图像的抓取
    def step_capture(self):
        # Retrieve left image
        self.zed.retrieve_image(self.image_frame, sl.VIEW.LEFT)
        # Retrieve depth map. Depth is aligned on the left image
        self.zed.retrieve_measure(self.depth_frame, sl.MEASURE.DEPTH)
        # Retrieve colored point cloud. Point cloud is aligned on the left image.
        self.zed.retrieve_measure(self.point_cloud, sl.MEASURE.XYZRGBA)

        # Get the data of the color frame and depth frame
        self.color_image = self.image_frame.get_data()
        self.color_image = cv2.cvtColor(self.color_image, cv2.COLOR_RGBA2RGB)           # (720, 1280, 3)
        self.depth_image = self.depth_frame.get_data()

        # reset
        self.map_image = self.map_src.copy()

    # 残影，估计不使用
    def record_residual(self):
        total_number = 500
        self.pre_obj_position.clear()
        if self.count >= total_number and self.count < total_number+self.residual_frame_count:
            for i in range(self.detected_number):
                tmp = []
                tmp.append(self.tmp_position_data[total_number - 1][i][0])
                tmp.append(self.tmp_position_data[total_number - 1][i][1])
                self.pre_obj_position.append(tmp)
        else:
            for i in range(self.detected_number):
                tmp = []
                tmp.append(self.tmp_position_data[self.count][i][0])
                tmp.append(self.tmp_position_data[self.count][i][1])
                self.pre_obj_position.append(tmp)

        for i in range(self.detected_number):
            tmp = np.zeros([2])
            err, world_coordinate = self.point_cloud.get_value(self.pre_obj_position[i][0], self.pre_obj_position[i][1])
            try:
                tmp[0] = round(self.MAP_WIDTH / 2 + world_coordinate[0] / self.AREA_WIDTH * self.MAP_WIDTH)
                tmp[1] = round(self.MAP_LENGTH - (world_coordinate[2] / self.AREA_LENGTH * self.MAP_LENGTH))
            except ValueError:
                if self.count == 0:
                    tmp = [0, 0]
                else:
                    tmp = self.points_res[i][0]
            self.points_res[i].insert(0, tmp)
            if len(self.points_res[i]) == self.residual_frame_count + 1:
                self.points_res[i].pop()

        self.map_image = np.zeros([self.MAP_LENGTH, self.MAP_WIDTH, 3])
        for i in range(self.detected_number):
            for j in range(len(self.points_res[i])):
                if j == 0:
                    cv2.circle(self.map_image, (int(self.points_res[i][j][0]), int(self.points_res[i][j][1])), 4, (255, 0, 0),
                               2)
                    cv2.circle(self.color_image, (int(self.pre_obj_position[i][0]), int(self.pre_obj_position[i][1])), 4,
                               (0, 0, 255), 2)
                else:
                    cv2.circle(self.map_image, (int(self.points_res[i][j][0]), int(self.points_res[i][j][1])), 4,
                               (255, 255, 255), 2)
                    cv2.circle(self.color_image, (int(self.pre_obj_position[i][0]), int(self.pre_obj_position[i][1])), 4,
                               (255, 0, 0), 2)

        self.count = (self.count+1) % (total_number+self.residual_frame_count)

        if self.count == total_number + self.residual_frame_count:
            for i in range(self.detected_number):
                self.points_res[i].clear()

    # 拍摄
    def capture(self):
        while True:
            # 抓取图像是否成功
            if self.zed.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                self.step_capture()

                # 获取并发送所有机车的位置
                self.GetCarRects()
                self.GetRectDepths()
                self.GetPos()
                self.get_map()
                # 与A板通信时使用
                # self.GetPack()
                # self.SendToAll()

                # Show images
                self.color_image[520:, 880:, :] = self.map_image
                cv2.namedWindow('Zed_color', cv2.WINDOW_AUTOSIZE)
                cv2.imshow('Zed_color', self.color_image)

                # Show Map
                map = cv2.resize(self.map_image, (800, 400))
                if self.left_mouse_down == True:
                    cv2.circle(map, (int(self.map_auto_x), int(self.map_auto_y)), 4, (0, 255, 255), 6)
                cv2.namedWindow('Map', cv2.WINDOW_AUTOSIZE)
                cv2.setMouseCallback('Map', self.map_on_mouse)
                cv2.imshow('Map', map)

                # reset
                self.car_rects.clear()
                self.car_depth_rects.clear()
                self.car_depth_positions.clear()
                self.car_map_positions.clear()
                self.message_positions.clear()

                if cv2.waitKey(1) > 0:
                    break


def read_test_data():
    points = []
    f = open('test_data.txt', 'r')
    data = f.read().split('\n')
    for line in data:
        dataxy = line.split(' ')
        pre_point = np.zeros([3, 2])
        for i in range(3):
            pre_point[i][0] = int(dataxy[i * 2])
            pre_point[i][1] = int(dataxy[i * 2 + 1])
        points.append(pre_point)
    return points


if __name__ == '__main__':
    camera = Camera()
    camera.capture()