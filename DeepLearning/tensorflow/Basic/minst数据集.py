import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

# 下载数据
mnist = input_data.read_data_sets('data/', one_hot=True)
print
print("类型: %s " % (type(mnist)))
print("训练数据有: %d " % (mnist.train.num_examples))
print("测试数据有: %d " % (mnist.test.num_examples))

trainimg = mnist.train.images # 28 * 28 * 1(颜色通道只有黑白) = 784
trainlabel = mnist.train.labels
testimg = mnist.test.images
testlabel = mnist.test.labels

print("数据类型 %s" %(type(trainimg)))
print("标签类型 %s" %(type(trainlabel)))
print("训练集的shape %s" %(trainimg.shape,))
print("测试集的标签shape %s" %(testlabel.shape,))

# 抽样显示5个mnist例子
nsample = 5
randidx = np.random.randint(trainimg.shape[0], size = nsample)
for i in randidx:
    curr_img = np.reshape(trainimg[i,:], (28, 28)) # 28 x 28的矩阵
    curr_label = np.argmax(trainlabel[i,:])
    plt.matshow(curr_img,cmap=plt.get_cmap('gray'))
    plt.show()

# 取batch操作
batch_size = 100
batch_xs, batch_ys = mnist.train.next_batch(batch_size)