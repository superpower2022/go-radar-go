import pyzed.sl as sl
import cv2
import time

from camera import Camera
from processor import Processor
from paint import Painter
from communicator.communicator import Communicator

# cmd id
MINIMAP = 0
MOVING = 1


def main():
    camera = Camera()

    if camera.error:
        print("fail to open Zed Camera!!!")
        return
    processor = Processor()
    painter = Painter()
    communicator = Communicator()
    while True:
        if camera.zed.grab(camera.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # get images from zed camera
            color_image, point_cloud_image = camera.step_capture()

            # processing data of images
            car_map_positions, message_positions, car_rects = processor.processing(color_image, point_cloud_image)

            # print('car map poslist :', car_map_positions)
            # print('send message list: ', message_positions)

            # draw color images and minimap
            painter.draw(car_map_positions, car_rects, color_image)

            if communicator.error_code == 0:
                 communicator.send(message_positions, MINIMAP)

            cv2.waitKey(1)
            # if cv2.waitKey(1) > 0:
            #     break
        else:
            cv2.destroyWindow('Zed_color')
            exit(-1)


if __name__ == '__main__':
    while True:
        main()
        print("restarting......")
        time.sleep(1)
