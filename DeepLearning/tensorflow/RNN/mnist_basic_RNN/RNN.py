import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
from tensorflow.examples.tutorials.mnist import input_data

sess = tf.Session()
mnist = input_data.read_data_sets('data', one_hot=True)
print(mnist.train.images.shape)

# 设置参数
lr = 1e-3
input_size = 28 # 每行输入28个特征点
timestep_size = 28 # 持续输入28行
hidden_size = 256 # 隐含层的数量
layer_num = 2 # LSTM layer的层数
class_num = 10 # 10分类问题

_X = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, class_num])

batch_size = tf.placeholder(tf.int32, [])
keep_prob = tf.placeholder(tf.float32,[])

# 定义网络结构
X = tf.reshape(_X, [-1, 28, 28])

def lstm_cell():
    cell = rnn.LSTMCell(hidden_size, reuse=tf.get_variable_scope().reuse)
    return rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)

# 堆叠两层LSTM


