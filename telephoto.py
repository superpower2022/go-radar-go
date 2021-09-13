import cv2
import time


CAP_WIDTH1 = 640
CAP_HEIGHT1 = 480

CAP_WIDTH2 = 640
CAP_HEIGHT2 = 480

WINDOW_WIDTH1 = 640
WINDOW_HEIGHT1 = 480

WINDOW_WIDTH2 = 640
WINDOW_HEIGHT2 = 480

WINDOW_X1 = 0
WINDOW_Y1 = 0

WINDOW_X2 = 0
WINDOW_Y2 = 550


if __name__ == '__main__':
    while True:
        capture1 = cv2.VideoCapture(0)
        capture2 = cv2.VideoCapture(2)
        if capture1.isOpened() and capture2.isOpened():
            # set camera width and length
            capture1.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH1)
            capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT1)

            capture2.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH2)
            capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT2)

            cv2.namedWindow("Screen1", 0)
            cv2.resizeWindow("Screen1", WINDOW_WIDTH1, WINDOW_HEIGHT1)
            cv2.moveWindow("Screen1", WINDOW_X1, WINDOW_Y1)

            cv2.namedWindow("Screen2", 0)
            cv2.resizeWindow("Screen2", WINDOW_WIDTH2, WINDOW_HEIGHT2)
            cv2.moveWindow("Screen2", WINDOW_X2, WINDOW_Y2)

            # read camera
            while True:
                # read
                read_code1, frame1 = capture1.read()
                read_code2, frame2 = capture2.read()

                if not read_code1 or not read_code2:
                    print('read failed....')
                    time.sleep(1)
                    break

                cv2.imshow("Screen1", frame1)

                cv2.imshow("Screen2", frame2)

                cv2.waitKey(1)
        else:
            time.sleep(1)
            print('telephoto-open filed!! Restart.... ')

    # while True:
    #     if capture1.isOpened():
    #         # set camera width and length
    #         capture1.set(cv2.CAP_PROP_FRAME_WIDTH, CAP_WIDTH1)
    #         capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, CAP_HEIGHT1)
    #
    #         # read camera
    #         while True:
    #             # read
    #             read_code1, frame1 = capture1.read()
    #
    #             if not read_code1:
    #                 print(123)
    #                 time.sleep(1)
    #                 continue
    #
    #             cv2.namedWindow("Screen1", 0)
    #             cv2.resizeWindow("Screen1", WINDOW_WIDTH1, WINDOW_HEIGHT1)
    #             cv2.moveWindow("Screen1", WINDOW_X1, WINDOW_Y1)
    #             cv2.imshow("Screen1", frame1)
    #
    #             cv2.waitKey(1)
    #     else:
    #         time.sleep(1)
    #         print('telephoto-open filed!! Restart.... ')
