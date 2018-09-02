import dataset
import tensorflow as tf
import time
from datetime import timedelta
import math
import random
import numpy as np

# 安装openCV 打开anaconda3的命令行，
# 运行命令conda install --channel https://conda.anaconda.org/menpo opencv3

# Adding Seed so that random initialization is consistent
from numpy.random import seed
seed(10)
from tensorflow import set_random_seed
set_random_seed(20)

batch_size = 32 #一次迭代32张图像，训练集一共1000张（猫500/狗500）

# Prepare input data
classes = ['dogs', 'cats']
num_classes = len(classes)

# 20% of the data will automatically be used for validation
validation_size = 0.2
img_size = 64 # 图片有大有小,但全连接大小固定，所以要求输入图像大小一致，设置为h=w=64
num_channels = 3 # 都是彩色图.jpg文件, channel = 3
train_path = 'training_data' # 训练数据文件夹目录

# We shall load all the training and validation images and labels into memory using openCV and
