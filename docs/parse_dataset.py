import random
import os
import argparse
import shutil

TRAIN = 0
VALID = 1
TEST = 2


def rmElems(ref_list, rm_list):
    for item in ref_list:
        rm_list.remove(item)


def splitData(in_list, ratio):
    """
    random.sample
    :param in_list: input list of dataset
    :param ratio: ratio of dataset
    :return: None
    """
    out_list = random.sample(in_list, int(total_data * ratio))
    rmElems(out_list, in_list)
    return out_list


def mvToImgDir(List, img_path, flag):
    """
    :param List: Data set list
    :param img_path: move path (dst path)
    :param flag: for what data set is
    :return: None
    """
    path = ''
    if flag == TRAIN:
        path = img_path + 'train/'
    elif flag == VALID:
        path = img_path + 'valid/'
    elif flag == TEST:
        path = img_path + 'test/'

    if not os.path.exists(path):
        os.mkdir(path)

    for file in List:
        from_img = imgs_path + file + '.jpg'
        to_img = path + file + '.jpg'
        shutil.move(from_img, to_img)


def mvToLabelDir(List, label_path, flag):
    """
    :param List: Data set list
    :param label_path: move path (dst path)
    :param flag: for what data set is
    :return: None
    """
    path = ''
    if flag == TRAIN:
        path = label_path + 'train/'
    elif flag == VALID:
        path = label_path + 'valid/'
    elif flag == TEST:
        path = label_path + 'test/'

    if not os.path.exists(path):
        os.mkdir(path)

    for file in List:
        from_label = annot_path + file + '.txt'
        if not os.path.exists(from_label):
            print(from_label, 'Not Found!')
            continue
        to_label = path + file + '.txt'
        shutil.move(from_label, to_label)


def writeToFile(List, flag):
    """
    Write the data list to current dir as "*flag*.txt"
    :param List: Data Set
    :return: None
    """
    filename = ''
    if flag == TRAIN:
        filename = 'train.txt'
    elif flag == VALID:
        filename = 'valid.txt'
    elif flag == TEST:
        filename = 'test.txt'

    f = open(filename, 'w')
    for index in List:
        f.write(index + '\n')
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='This is program of setting RATIO of DATASET for yolo-v5.'
                    'Here we will have train, valid and test sets.'
                    '!!For PATH, we auto add / at the end!!')
    parser.add_argument('-train', type=int, default=70, help='train ratio, default with 70')
    parser.add_argument('-valid', type=int, default=20, help='valid ratio, default with 20')
    parser.add_argument('-data_path', type=str, default='.', help='root path of DATASET, default with "./"')
    parser.add_argument('-out_path', type=str, help='move data to DataSets path', required=True)
    opt = parser.parse_args()

    # Normalized to 0-1
    train_ratio = opt.train / 100
    valid_ratio = opt.valid / 100
    test_ratio = 1 - train_ratio - valid_ratio

    if test_ratio < 0:
        print('Ratio must be LEGAL！')
        exit(-1)

    # Parse file path, add '/' to the end
    global imgs_path, annot_path, out_path
    dataset_path = opt.data_path + '/'
    imgs_path = dataset_path + 'images/'
    annot_path = dataset_path + 'annotations/'
    out_path = opt.out_path + '/'

    if not (os.path.exists(imgs_path) or os.path.exists(annot_path)):
        print('Data Path must organized with "/images" and "/annotations"')
        exit(-1)

    # Extract File Name without postfix
    data, train_data, valid_data, test_data = [], [], [], []
    for img in os.listdir(imgs_path):
        data.append(img[:-4])

    total_data = len(data)
    print('Total data:', total_data)

    train_data = splitData(data, train_ratio)
    valid_data = splitData(data, valid_ratio)
    test_data = data.copy()
    print('Train data:', len(train_data))
    print('Valid data:', len(valid_data))
    print('Test data:', len(test_data))

    # Write dataset to file
    writeToFile(train_data, TRAIN)
    writeToFile(valid_data, VALID)
    writeToFile(test_data, TEST)

    # Move the dataset to Destination
    mv_img_path = out_path + 'images/'
    mv_label_path = out_path + 'labels/'

    if not os.path.exists(mv_img_path):
        os.mkdir(mv_img_path)
    if not os.path.exists(mv_label_path):
        os.mkdir(mv_label_path)

    mvToImgDir(train_data, mv_img_path, TRAIN)
    mvToImgDir(valid_data, mv_img_path, VALID)
    mvToImgDir(test_data, mv_img_path, TEST)

    mvToLabelDir(train_data, mv_label_path, TRAIN)
    mvToLabelDir(valid_data, mv_label_path, VALID)
    mvToLabelDir(test_data, mv_label_path, TEST)
    print("Done! Enjoy!")
