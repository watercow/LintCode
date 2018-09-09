import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
from tensorflow.examples.tutorials.mnist import input_data

sess = tf.Session()
mnist = input_data.read_data_sets('data', one_hot=True)
print(mnist.train.images.shape)

# 设置参数
lr = 1e-3
input_size = 28
