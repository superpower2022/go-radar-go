## 使用自己的数据集训练(yolov5)

[TOC]

### 获得标注的数据集

这里选择官方的2019比赛导播视角的数据集

[DJI ROCO](https://pan.baidu.com/s/1Ezh1ip8ZOLJeVzhBD9JuOQ)（百度网盘）提取码：ytls

数据集文件结构

```shell
/
├─robomaster_Central China Regional Competition
│  ├─image
│  └─image_annotation
├─robomaster_Final Tournament
│  ├─image
│  └─image_annotation
├─robomaster_North China Regional Competition
│  ├─image
│  └─image_annotation
└─robomaster_South China Regional Competition
    ├─image
    └─image_annotation
```

### 将官方标注文件xml处理成yolo归一化文件txt

处理的脚本文件为`parse_to_txt.py`

```shell
$ python parse_to_txt.py -xml_dir_path /xx/xx -out_dir_path /xxx
```

```shell
$ python parse_to_txt.py -h
usage: parse_to_txt.py [-h] -xml_dir_path XML_DIR_PATH -out_dir_path OUT_DIR_PATH

This is program of pre-processing xml to txt for yolo-v5

optional arguments:
  -h, --help            show this help message and exit
  -xml_dir_path XML_DIR_PATH
                        input xml annotation dir path
  -out_dir_path OUT_DIR_PATH
                        output txt annotation dir path
```

处理逻辑为：

1. 输入存放xml文件根目录，例如`./DJI_ROCO/robomaster_Final_Tournament/image_annotation`（需要注意的是目录**不能有空格**）
2. 输入存放txt文件的根目录，例如`./DJI_Data/annotations`（同样需要注意1.的问题）

脚本会解析**3种object**，按照列表顺序为`['car', 'watcher', 'armor']`，即0，1，2的顺序

如果需要更改可以修改文件中如下的代码（需要与数据集存在的object对应）

```python
...
# parse object class index
classindex = -1
if objname == 'car':
    classindex = 0
elif objname == 'watcher':
    classindex = 1
elif objname == 'armor':
    classindex = 2
...
```

### 将官方数据集分成合理的训练比例

处理脚本文件为`parse_dataset.py`

```shell
$ parse_dataset.py -out_path /xx/xx
```

```shell
$ python parse_dataset.py -h
usage: parse_dataset.py [-h] [-train TRAIN] [-valid VALID] [-data_path DATA_PATH] -out_path OUT_PATH

This is program of setting RATIO of DATASET for yolo-v5.Here we will have train, valid and test sets.!!For PATH, we
auto add / at the end!!

optional arguments:
  -h, --help            show this help message and exit
  -train TRAIN          train ratio, default with 70
  -valid VALID          valid ratio, default with 20
  -data_path DATA_PATH  root path of DATASET, default with "./"
  -out_path OUT_PATH    move data to DataSets path
```

处理逻辑为：

1. 默认`train`的比例为85%，`valid`的比例为10%，`test`的比例为5%，需要更改只需改前两个比例

2. 数据集的位置默认为脚本文件**当前的目录**，需要按照如下**目录树安排**

   ```shell
   /
   ├─DJI_Data
   │  ├─images
   │  └─annotations
   ```

   即把各自类型所有的数据**统一放置**在一起

3. 输出目录选择一个空的目录，例如`./DJI`，脚本会自动创建好yolo训练的目录结构，例如

   ```shell
   DJI/
      ├─images
      │  ├─test
      │  ├─train
      │  └─valid
      ├─labels
      │  ├─test
      │  ├─train
      │  └─valid
   ```

### Enjoy~

最后附上我参考的官方的教程，[传送门](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

