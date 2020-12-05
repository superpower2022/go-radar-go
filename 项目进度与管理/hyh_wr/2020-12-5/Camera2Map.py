import pyrealsense2 as rs
import numpy as np
import cv2



class Camera:
    WIDTH = 640
    HEIGHT = 480
    MAP_WIDTH = 300
    MAP_LENGTH = 600
    AREA_LENGTH = 2.1
    AREA_WIDTH = 1.05
    # camera x y to map x y
    alpha = 0.70

    def __init__(self):
        self.pipeline = rs.pipeline()

        # Configure depth and color streams
        my_config = rs.config()
        my_config.enable_stream(rs.stream.depth, self.WIDTH, self.HEIGHT, rs.format.z16, 30)
        my_config.enable_stream(rs.stream.color, self.WIDTH, self.HEIGHT, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(my_config)

        # present frame data
        self.pre_frame = None

        # present depth frame data
        self.depth_frame = None

        # present color frame data
        self.color_frame = None

        # present color numpy array
        self.color_image = None

        # present depth numpy array
        self.depth_image = None

        # record some data for initializing the map
        self.top_x = 0
        self.top_y = 0
        self.down_y = 0
        self.down_x = 0

        self.top_distance = 0
        self.down_distance = 0

        self.camera_height = 0.5

        # record the position of mouse on the small map
        self.map = np.zeros([self.MAP_LENGTH, self.MAP_WIDTH])
        self.map_x = 0
        self.map_y = 0

        # present mouse position
        self.X = self.WIDTH // 2
        self.Y = self.HEIGHT // 2

        # present distance
        self.dist = 0.0

    def get_frame(self):
        self.pre_frame = self.pipeline.wait_for_frames()

    def update_frame(self):
        self.depth_frame = self.pre_frame.get_depth_frame()
        self.color_frame = self.pre_frame.get_color_frame()
        if not self.depth_frame or not self.color_frame:
            return
        # Convert images to numpy arrays
        self.depth_image = np.asanyarray(self.depth_frame.get_data())
        self.color_image = np.asanyarray(self.color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        self.depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)

    def get_distance(self):
        self.dist = self.depth_frame.get_distance(self.X, self.Y)

    def step_capture(self):
        self.get_frame()
        self.update_frame()
        self.images = np.hstack((self.color_image, self.depth_colormap))

    def capture(self):
        self.count = 0
        while True:
            self.step_capture()

            # Show images
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.setMouseCallback('RealSense', self.on_mouse)
            cv2.circle(self.images, (self.X, self.Y), 4, (255, 0, 0), 2)
            cv2.imshow('RealSense', self.images)

            # Show images
            cv2.namedWindow('Map', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('Map', self.map)

            if cv2.waitKey(1) > 0:
                break

    def on_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.X = x % self.WIDTH
            self.Y = y % self.HEIGHT
            self.get_distance()
            # print(self.dist)
            # init
            if self.count < 2:
                self.count += 1
                if self.down_y == 0:
                    self.down_y = self.Y
                    self.down_x = self.X
                    self.down_distance = self.dist
                elif self.down_y > self.Y:
                    self.top_y = self.Y
                    self.top_x = self.X
                    self.top_distance = self.dist
                else:
                    self.top_y = self.down_y
                    self.top_x = self.down_x
                    self.top_distance = self.down_distance
                    self.down_y = self.Y
                    self.down_x = self.X
                    self.down_distance = self.dist

                if self.count == 2:
                    self.down_distance = np.sqrt(np.square(self.down_distance) - np.square(self.camera_height))
                    self.top_distance = np.sqrt(np.square(self.top_distance) - np.square(self.camera_height))
                print("%f\t\t%f" % (self.top_distance, self.down_distance))
            else:
                if self.dist > 0.0:
                    self.get_map()
            #print("(%d, %d)" % (self.X, self.Y))


    def get_map(self):
        self.compute_coordinate_of_map()
        self.map = np.zeros([self.MAP_LENGTH, self.MAP_WIDTH])
        cv2.circle(self.map, (self.map_x, self.map_y), 4, (255, 0, 0), 2)

    def compute_coordinate_of_map(self):
        distance_y = (self.Y - self.down_y)/(self.top_y - self.down_y)*(self.top_distance - self.down_distance)+self.down_distance
        x = (np.sqrt(np.square(self.camera_height)+np.square(distance_y))-self.dist)/np.sqrt(self.camera_height/distance_y+1)
        t = self.camera_height * x / distance_y
        distance_y -= x
        #distance_x = np.sqrt(np.square(self.dist) - np.square(self.camera_height - t) - np.square(distance_y) +0.1)

        # print("distance_x:%f\tdistance_y:%f\tdist:%f" % (distance_x, distance_y, self.dist))

        # if self.X > (self.top_x+self.down_x) /2:
        #     self.map_x = int(self.MAP_WIDTH/2 + distance_x/self.AREA_WIDTH*self.MAP_WIDTH)
        # else:
        #     self.map_x = int(self.MAP_WIDTH/2 - distance_x/self.AREA_WIDTH*self.MAP_WIDTH)
        self.map_x = int(self.MAP_WIDTH / 2 + (self.X - (self.top_x + self.down_x) / 2) * distance_y * self.alpha)

        self.map_y = self.MAP_LENGTH-int(distance_y/self.AREA_LENGTH*self.MAP_LENGTH)
        print("map x:", self.map_x, "map y:", self.map_y)


if __name__ == '__main__':
    camera = Camera()
    camera.capture()