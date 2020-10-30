#  雷达站算法汇报
***
##  1.功能实现
目前实现功能：

> 	1.实现对视野内比赛机器人的目标识别、跟踪与预测。
> 	2.实现对目标三维坐标的获取，距离与偏转角度的测量。
> 	3.实现到二维小地图的投影变换。

##  2.模块划分	
主要分为三个模块:识别(detect)、跟踪(track)和定位(locate)。

**系统环境：**

> Ubuntu16.04
>
> python 3.8 + pytorch1.6 + torchvision0.6 （安装教程： https://xugaoxiang.com/2020/06/17/yolov5/）
>
> yolov5 ： https://github.com/ultralytics/yolov5/releases



###  2.1 目标识别

该模块主要借助yolov5实现目标的检测。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809082216739.png)
可以把yolov5看做是基于pytorch的深度神经网络，输入一张图片，可以得到一个检测目标的list。

####  准备工作

参考教程：《How to Train YOLO v5 on a Custom Dataset》https://www.youtube.com/watch?v=MdF6x6ZmLAY

**1.收集样本与标签:**

> 使用的是Robomaster2019数据集
> https://terra-1-g.djicdn.com/b2a076471c6c4b72b574a977334d3e05/resources/DJI%20ROCO.zip
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808213945757.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808213904144.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)

**2.数据集的整理**

> 使用ROBOFLOW进行了数据集的划分，符合yolov5的训练格式
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200809082235427.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808214112406.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)

 **3.训练模型**

> 使用谷歌Colab的GPU加速训练 
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/202008090822548.png)
> 这是我用于训练的yolo文件和数据集
>  yolo文件 : 
>     https://drive.google.com/drive/folders/1AljyGyvVakW7KfDPz2uR59ijgccJpBW1?usp=sharing
> 训练数据集 : 
> https://drive.google.com/drive/folders/1kYUnsWFqHcAH7FvKZEJzFUPee8uzidRC?usp=sharing
>   最终得到权重文件 :   
>   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808214931362.png)

#### 使用方法 : 
```python
#载入事先训练好的模型
model = Ensemble()
model.append(torch.load(weights, map_location=map_location)['model'].float().fuse().eval())['model'].float().fuse().eval()) 
#对图像img进行推断        
pred = models(img)[0]
```
这是推断返回的list:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808212651554.png)
[x1,y1,x2,y2,置信度,类别] (xy1为左上点 ,xy2为右下点)
#### 实现效果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808212416751.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)

###  2.2 目标识别
将第一个模块检测到的目标框传入DEEP-SORT框架中，实现目标的追踪和预测。

deep-sort 详见：《[Deep SORT多目标跟踪算法代码解析](https://www.cnblogs.com/pprp/articles/12736831.html) 》https://www.cnblogs.com/pprp/articles/12736831.html

> 	核心组件： 		
> 目标框: 进过yolo算法提取的目标框 		
> 轨迹:  目标框连续匹配成功若干次所形成的一个轨迹，拥有自己的标号。标号有两个状态：确定与不确定，一旦连续未匹配次数超过上限，就会变成不确定态，即不再显示。
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808221331495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)
>  设置了`目标(detection)`队列(且每个目标有两种状态)与`轨迹(track)`队列。
      通过`yolo`算法实现对detection的提取，判断进入队列。
      对于新进入的detection，我们通过`CNN(ReID)`进行特征(feature)的提取。
      然后对这一帧提取到的detection，与上一帧的track预测进行`级联匹配`(feature 与 metric的匹配)，从而实现目标的跟随。
     最后再到图上回显出来，并进行后续操作。

####  级联匹配
涉及到特征与几何的余弦距离、马氏距离和匈牙利算法。

距离：

> 集中体现在这个矩阵中：
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808222106129.png)
> 		两个N维特征主元素相比较，通过某种标准下的运算，就可以得到一个衡量相似度的数值(越小，相似度越高)。
> 		所以矩阵的第i行j个的含义就是上一帧中第i个目标框与下一帧第j个目标框之间的相似度。 		
> 			  例如： CNN提取出N维的特征向量和当前卡尔曼滤波需要的当前位置向量(x,y,w,h,vx,vy,vw,vh)

匈牙利算法：

> 主要体现在这两个向量中：0.28743720054626465 s
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808222344118.png)
> 	 		给出相似度的最佳匹配组合。
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808222617403.png)
>
> #### 实现效果：	
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808222827173.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)
> ###  2.3 定位与投影变换
> 通过pnp算法实现目标三维坐标的还原，可以计算出偏转角与距离。再从相机坐标系转到物体坐标系。最后再到图上回显出来，并进行后续操作。
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808223035604.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)
> ####  实现效果：
> ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200808223117130.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg1MTE0OQ==,size_16,color_FFFFFF,t_70)
>


