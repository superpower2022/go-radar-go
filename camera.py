import pyzed.sl as sl
import numpy as np
import cv2


class Camera(object):
    """
    With this Camera class, you can use zed camera to capture images, and
    all the useful information will be transformed into numpy array
    """
    # size of camera window
    WIDTH = 1280
    HEIGHT = 720

    # Camera BrightNess
    ZED_BRIGHTNESS = 4

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

        # origin brightness 4
        # Set Camera Brightness
        self.zed.set_camera_settings(sl.VIDEO_SETTINGS.BRIGHTNESS, self.ZED_BRIGHTNESS)
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

        # present point cloud numpy array
        self.point_cloud_image = None

        # The present xyz of the point
        self.world_coordinate = None

    # get a frame
    def step_capture(self) -> (np.ndarray, np.ndarray):
        """
        @func: capture the present images from the zed camera including color image
        and point cloud image.
        return: self.color_image, self.point_cloud_image
        """
        # Retrieve left image
        self.zed.retrieve_image(self.image_frame, sl.VIEW.LEFT)

        # Retrieve depth map. Depth is aligned on the left image
        # self.zed.retrieve_measure(self.depth_frame, sl.MEASURE.DEPTH)

        # Retrieve colored point cloud. Point cloud is aligned on the left image.
        self.zed.retrieve_measure(self.point_cloud, sl.MEASURE.XYZRGBA)

        # Get the data of the color frame ,depth frame and point cloud
        self.color_image = self.image_frame.get_data()
        self.color_image = cv2.cvtColor(self.color_image, cv2.COLOR_RGBA2RGB)           # (720, 1280, 3)
        # self.depth_image = self.depth_frame.get_data()
        self.point_cloud_image = self.point_cloud.get_data()
        self.point_cloud_image[np.isnan(self.point_cloud_image)] = 0  # change the value of "nan" to 0
        self.point_cloud_image[np.isinf(self.point_cloud_image)] = 0  # change the value of "inf" to 0
        return self.color_image, self.point_cloud_image
