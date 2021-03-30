import pyzed.sl as sl
import cv2

from camera import Camera
from processor import Processor
from paint import Painter
from communicator.communicator import Communicator

# cmd id
MINIMAP = 0
MOVING = 1


def main():
    camera = Camera()
    processor = Processor()
    painter = Painter()
    communicator = Communicator()
    while True:
        # 抓取图像是否成功
        if camera.zed.grab(camera.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # get images from zed camera
            color_image, point_cloud_image = camera.step_capture()

            # processing data of images
            car_map_positions, message_positions, car_rects = processor.processing(color_image, point_cloud_image)

            # draw color images and minimap
            painter.draw(car_map_positions, car_rects, color_image)

            if communicator.error_code == 0:
                communicator.send(message_positions, MINIMAP)

            if cv2.waitKey(1) > 0:
                break


if __name__ == '__main__':
    main()
