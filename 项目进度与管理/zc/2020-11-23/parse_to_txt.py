import xml.etree.cElementTree as ET
import argparse
import os


def normalized_xywh(points, imgsize):
    """
    :param points: (x_min, y_min, x_max, y_max) for min points is upper-left, max is bottom-right
    :param imgsize: (width, height) for the height and width of a img
    :return: (x_center, y_center, box_width, box_height), normalized into 0-1
    """
    box_width = points[2] - points[0]
    box_height = points[3] - points[1]
    x_center = (points[0] + points[2]) / 2.0
    y_center = (points[1] + points[3]) / 2.0

    # normalized
    box_width /= imgsize[0]
    x_center /= imgsize[0]
    box_height /= imgsize[1]
    y_center /= imgsize[1]

    return x_center, y_center, box_width, box_height


def parse_xml(xml):
    """
    :param xml: the root tree of xml
    :return: (obj_class, obj_x_center, obj_y_center, obj_width, obj_height)
    """
    imgwidth = int(xml.find('size').find('width').text)
    imgheight = int(xml.find('size').find('height').text)

    diff_skip_cnt = 0
    objclass_skip_cnt = 0

    for object in xml.iterfind('object'):
        objname = object.find('name').text
        objxmin = float(object.find('bndbox').find('xmin').text)
        objymin = float(object.find('bndbox').find('ymin').text)
        objxmax = float(object.find('bndbox').find('xmax').text)
        objymax = float(object.find('bndbox').find('ymax').text)
        objdiff = object.find('difficulty')

        # drop over boundary
        if (objxmin < 0 or objxmin > imgwidth) or \
                (objxmax < 0 or objxmax > imgwidth) or \
                (objymin < 0 or objymin > imgheight) or \
                (objymax < 0 or objymax > imgheight):
            diff_skip_cnt += 1
            continue

        # Skip the Obscuration > 20%
        if objdiff is not None:
            objdiff = int(objdiff.text)
            if objdiff == 1:
                diff_skip_cnt += 1
                continue

        # parse object class index
        classindex = -1
        if objname == 'car':
            classindex = 0
        elif objname == 'watcher':
            classindex = 1
        elif objname == 'armor':
            classindex = 2

        if classindex == -1:
            objclass_skip_cnt += 1
            continue

        objx_cen, objy_cen, obj_width, obj_height = normalized_xywh((objxmin, objymin, objxmax, objymax),
                                                                    (imgwidth, imgheight))

        yield classindex, objx_cen, objy_cen, obj_width, obj_height

    print('objclass skip count:%2d, objdifficulty skip count:%2d\n' % (objclass_skip_cnt, diff_skip_cnt))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is program of pre-processing xml to txt for yolo-v5')
    parser.add_argument('-xml_dir_path', type=str, help='input xml annotation dir path', required=True)
    parser.add_argument('-out_dir_path', type=str, help='output txt annotation dir path', required=True)
    opt = parser.parse_args()

    xmlpath = opt.xml_dir_path + '/'
    outpath = opt.out_dir_path + '/'

    xmlList = os.listdir(xmlpath)
    for xml in xmlList:
        xmlname = xml.split('.')
        print(xmlname[0])
        filePath = xmlpath + xml
        xmlroot = ET.parse(filePath)
        txtfilepath = outpath + xmlname[0] + '.txt'
        txt = open(txtfilepath, 'w')
        for obj_class, obj_x_center, obj_y_center, obj_width, obj_height in parse_xml(xmlroot):
            txt.write('%d %f %f %f %f\n' % (obj_class, obj_x_center, obj_y_center, obj_width, obj_height))
        txt.close()
