# coding:utf-8
'''
此文件实现地面机器人的目标检测
后续优化 ：
    1.分类只选取地面机器人的车身，然后对车身内部进行常规装甲板匹配（权重文件重新训练
    2.加入测距与放射变换
    3.DEEP_SORT 内部需要特征提取的分类器
    修改日期：07.22 truth 初步完成车身识别 , 加入了DEEP_SORT，自带卡尔曼滤波
    修改日期：07.28 truth 添加pnp测距 实现三维坐标的获取
                    Josef 添加了小地图和红蓝筛选
'''
################## 头文件 ##################
import argparse
import torch.backends.cudnn as cudnn
#yolo
from yolov5.utils.datasets import *
from yolov5.models.experimental import attempt_load
from yolov5.utils.my_utils import *
#自己定义的小工具
from tools.draw import *
from tools.rotate_bound import *
from tools.parser import *
#deep——sort
from deep_sort import *
#测距
from pnp.config import *
from pnp.tools import *
#系统
import cv2 as cv
import numpy as np
import math
############################################

#路径
<<<<<<< HEAD
cur_dir = '/home/zc/go-radar-go/'
=======
cur_dir = 'D:/P2/202012/WeatherReport/go-radar-go/'
>>>>>>> bae516871e02ff5d84bad28bfdfb18ad44683849

'''
相机参数 size画面尺寸
       focal_len 焦距？
'''
size =[1920,886]
focal_len = 3666.666504
cameraMatrix = np.array(
            [[focal_len, 0, size[0]/2],
             [0, focal_len, size[1]/2],
             [0, 0, 1]],dtype=np.float32)

distCoeffs =  np.array( [-0.3278216258938886, 0.06120460217698008,
              0.003434275536437622, 0.009257102247244872,
              0.02485049439840001])
device_ = '0'

#权重
weights = cur_dir + 'yolov5/weights/last_yolov5s_0722.pt'
#输入文件目录
source = cur_dir + 'yolov5/inference/images'  # file/folder, 0 for webcam
#输出文件目录
out = cur_dir + 'yolov5/inference/output'  # output folder
#固定输入大小？
imgsz = 640  # help='inference size (pixels)')
#置信度阈值
conf_thres = 0.4
#iou合并阈值
iou_thres = 0.3
#deep_sort configs
deep_sort_configs=cur_dir + 'configs/deep_sort.yaml'
#测试视频
video_in = cur_dir + 'data/t1.mp4'
#标定小地图
map_dir = cur_dir + 'pnp/map2019.png'
classes = ''
agnostic = ''
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def adjustImgSize(im0s,imgsz,device):
    '''
    brief@ 调整图像的属性
    param@ im0s: the original input by cv.imread
           imgsz: the size
    return@ img for input
    '''
    # Padded resize
    img = letterbox(im0s, new_shape=imgsz)[0]
    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)
    #转成tensor
    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    return img

def detectPerFrame(im0s):
    '''
    brief@ 进行逐帧检测
    param@ im0s:
    return@ bbox_xywh(是个二维数组，第一维为目标的下标，第二维依次为目标中心点的坐标([0:2]=>x_center,y_center)),
            cls_conf 置信度,
            cls_ids  目标标号
    need two images 
        @ img  is the adjusted image as the input of the DNN
        @ im0s is the orignial image
    '''
    #调整一下图像大小
    img = adjustImgSize(im0s, imgsz, device)
    # inference 推断
    pred = models(img)[0]
    #极大值抑制
    pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic)

    bbox_xcycwh = []
    cls_conf  = []
    cls_ids   = []
    # Process detections 得到单位是六维向量的数组
    for i, det in enumerate(pred):  # detections per image
        '''
        pred is a tensor list which as six dim
            @dim 0-3 : upper-left (x1,y1) to right-bottom (x2,y2) 就是我们需要的矩形框
            @dim 4 confidence 
            @dim 5 class_index 类名
        '''
        # gn = torch.tensor(im0s.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        if det is not None and len(det):
            # 选择前四项，作为缩放依据 Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0s.shape).round()
            cls_conf = det[:, 4]
            cls_ids  = det[:, 5]

            # # Draw rectangles
            for *xyxy, conf, cls in det:
                xywh=[(xyxy[0]+xyxy[2])/2, (xyxy[1]+xyxy[3])/2, xyxy[2]-xyxy[0], xyxy[3]-xyxy[1]]
                bbox_xcycwh.append(xywh)
    return bbox_xcycwh, cls_conf, cls_ids


def PNPsolver(target_rect,cameraMatrix,distCoeffs):
    '''
    解算相机位姿与获取目标三维坐标
    Parameters
    ----------
    target_center :目标矩形点集 顺序为 左上-右上-左下-右下
    cameraMatrix
    distCoeffs

    Returns  tvec(三维坐标), angels(偏转角度:水平,竖直 ) , distance(距离)
    -------
    '''
    #标定板的尺寸
    halfwidth =  145 / 2.0
    halfheight = 210 / 2.0
    # 标定板的角点
    objPoints\
        =  np.array([[-halfwidth,  halfheight, 0],
           [halfwidth,  halfheight, 0],
           [halfwidth, -halfheight, 0],
           [-halfwidth, -halfheight, 0]  #bl
           ] ,dtype=np.float64)
    model_points = objPoints[:, [0, 1, 2]]
    i = 0
    target = []
    #将八个点中 两两组合
    while(i<8):
        target.append([target_rect[i], target_rect[i+1]])
        i= i+2
    target=np.array(target,dtype=np.float64)
    #解算 retval为成功与否
    retval,rvec,tvec = cv.solvePnP(model_points,target,cameraMatrix,distCoeffs)
    if retval == False :
        print("PNPsolver failed !")
        return [0, 0, 0], [0, 0], 0
    # print(rvec)
    x = tvec[0]
    y = tvec[1]
    z = tvec[2]

    angels = [math.atan2(x, z),                       #水平偏角
              math.atan2(y, math.sqrt(x * x + z * z))]#竖直偏角
    distance = math.sqrt(x * x + y * y + z * z)
    return tvec , angels , distance

def getCornerPoints(bbox_xyxy):
    '''
    Parameters
    ----------
    bbox_xyxy (是个二维数组，第一维为目标的下标，第二维依次为目标左上点的坐标([0:2]=>x1,y1) 目标右下点的坐标([2:4]=>x2,y2) ),
    Returns points 四个点 (是个二维数组，第一维为目标的下标，第二维是四个点 顺序为 左上-右上-左下-右下 ),
    -------
    '''
    points = []
    bbox_tl = bbox_xyxy[:, 0:2]
    bbox_tr = np.array([bbox_xyxy[:, 2], bbox_xyxy[:, 1]]).transpose()
    bbox_br = bbox_xyxy[:, 2:4]
    bbox_bl = np.array([bbox_xyxy[:, 0], bbox_xyxy[:, 3]]).transpose()
    points = np.concatenate((bbox_tl, bbox_tr), axis=1)
    points = np.concatenate((points, bbox_br), axis=1)
    points = np.concatenate((points, bbox_bl), axis=1)
    return points

def get3Dposition(bbox_clockwise):
    '''
    结算
    '''
    angels = []
    distance = []
    tvec = []
    for i in range(len(bbox_clockwise)):
        tvec_cur, angels_cur, distance_cur = PNPsolver(bbox_clockwise[i], cameraMatrix, distCoeffs)

        tvec.append(tvec_cur)
        angels.append(angels_cur)
        distance.append(distance_cur)
    return tvec, angels, distance


#主函数开始啦
if __name__ == "__main__":
    ############################初始化步骤###################################
    #载入小地图
    '''
    flag = torch.cuda.is_available()
    print(flag)
    exit(0)
    '''
    lm = little_map(map_dir)
    # Initialize 找GPU
    device = torch_utils.select_device(device_)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model载入模型
    models = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=models.stride.max())  # check img_size
    
    if half:
        models.half()  # to FP16
    
    # Get names and colors获得类名与颜色
    names = models.module.names if hasattr(models, 'module') else models.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]
    cfg = get_config(deep_sort_configs)

    #初始化deepsort
    my_deepsort = build_tracker(cfg, torch.cuda.is_available())
    my_deepsort.device = device
    ######################################################################

    ############################调整相机和小地图大小#############################
    #获取摄像头信息
    cap = cv.VideoCapture(video_in) 
    cap_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cap_fps = cap.get(cv2.CAP_PROP_FPS)# 读取视频的fps
    cap_size = (cap_width, cap_height)#大小
    cap_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))    # 读取视频时长（帧总数）

    print("fps: {}\nsize: {}".format(cap_fps, cap_size))
    print("lm size:({},{})".format(lm.map_width, lm.map_height))
    print("[INFO] {} total frames in video".format(cap_total))

    height, width = cap_width,cap_height
    fixed_width = 800
    fixed_height = 0
    #小地图的大小
    show_width = lm.map_width
    show_height = lm.map_height
    
    #越界保护，保证长方形形状
    if cap_width > fixed_width:
        fixed_height = int(fixed_width / width * height)
    else:
        fixed_width = width
        fixed_height = height
    resize_ratio = show_width / fixed_width

    #输出带有框图记录的视频流
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out_2 = cv2.VideoWriter('map2019.avi', fourcc, 20.0, ( int(lm.get_width()*0.5),int(lm.get_height()*0.5)))
    ######################################################################

    bbox_tlwh  = [] ; bbox_xyxy  = []
    identities = [] ; tvec = []
    angels = [] ; distance = []

    while True:
        ret, frame = cap.read()# BGR
        if ret == True:
            ####你们应该不需要这么做rotate my video 因为视频是歪的= =
            height, width = frame.shape[:2]
            if height > width :
                im0s = rotate_bound(frame, -90)#
            else:
                im0s = frame  #
            im0s = cv2.resize(im0s, (int(fixed_width), int(fixed_height)))

            ########################计时 核心过程！########################
            t1 = torch_utils.time_synchronized()
            #yolo目标检测
            bbox_xcycwh, cls_conf, cls_ids = detectPerFrame(im0s)
            t2 = torch_utils.time_synchronized()
            print('yolo:', t2 - t1, "s")

            #目标跟踪 output = [x1,y1,x2,y2,track_id]
            outputs,bbox_vxvy = my_deepsort.update(bbox_xcycwh, cls_conf, im0s)
            t3 = torch_utils.time_synchronized()
            print('deep:', t3 - t2, "s")
            #############################################################

            ########################计算每个装甲板的位姿信息########################
            if len(outputs) > 0:
                bbox_tlwh = []
                bbox_xyxy = outputs[:, :4]
                identities = outputs[:, 4]
                #得到角点信息
                bbox_clockwise = getCornerPoints(bbox_xyxy)
                #计算每个目标的偏转角度与距离
                tvec, angels, distance = get3Dposition(bbox_clockwise)
            #############################################################

            armor_color = getArmorColor(im0s, bbox_xyxy)
            bbox_xyxy_show = []
            bbox_vxvy_show = []

            ########################对于每个目标进行可视化########################

            #准备好所有位置和速度标注
            for i in range(len(outputs)):
                #打印出具体位置
                bbox_show = []
                #打印出运动状态（根据kalmanfilter得到的速度）
                motion_show = []
                bbox_vxvy_len = len(bbox_vxvy[0])
                for j in range(len(bbox_xyxy[i])):
                    bbox_show.append(bbox_xyxy[i, j]*resize_ratio)
                    if j < bbox_vxvy_len :
                        motion_show.append(bbox_vxvy[i, j]*resize_ratio)
                bbox_xyxy_show.append(bbox_show)
                bbox_vxvy_show.append(motion_show)

            #打印到相机图
            for_show = cv2.resize(im0s, (show_width, show_height))
            for_show = draw_boxes(for_show, bbox_xyxy_show, angels, distance, tvec, identities)

            #在小地图上显示
            center = getRectCenterpoint(bbox_xyxy_show)
            cur_pic = showLittleMap(lm, center, bbox_vxvy_show,identities,armor_color)
            #############################################################
            t4 = torch_utils.time_synchronized()
            print('show:', t4 - t3, "s")

            cv.imshow('map', cur_pic)
            cv2.imshow("for_show", for_show)
            #out_2.write(cur_pic)
            cv2.waitKey(1)
        else:
            break

    cap.release()
    cv.destroyAllWindows()
