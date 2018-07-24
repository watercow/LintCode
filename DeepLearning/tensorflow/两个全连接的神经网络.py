#===========================
# 最简单的全连接神经网络
# 第一层输入:784个单元(28 * 28 * 1)
# 隐含层(1层):50个单元
# 输出层:10个单元(预测结果0-9)
# 再加一个softmax
#===========================
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/", one_hot=True)

# 参数设置
numClasses = 10
inputSize = 784
numHiddenUnits = 50
trainingIterations = 10000
batchSize = 100

X = tf.placeholder(tf.float32, shape=[None, inputSize])
y = tf.placeholder(tf.float32, shape=[None, numClasses])

# 参数初始化



