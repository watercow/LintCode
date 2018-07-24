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
W1 = tf.Variable(tf.truncated_normal([inputSize, numHiddenUnits], stddev = 0.1))
B1 = tf.Variable(tf.constant(0.1), [numHiddenUnits])
W2 = tf.Variable(tf.truncated_normal([numHiddenUnits, numClasses], stddev = 0.1))
B2 = tf.Variable(tf.constant(0.1), [numClasses])

# 网络结构
hiddenLayerOutput = tf.matmul(X,W1) + B1
hiddenLayerOutput = tf.nn.relu(hiddenLayerOutput)
finalOutput = tf.matmul(hiddenLayerOutput, W2) + B2
finalOutput = tf.nn.relu(finalOutput)

# 网络迭代
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=finalOutput)) # labels真实值 logits预测值
opt = tf.train.GradientDescentOptimizer(learning_rate=.1).minimize(loss)

correct_prediction = tf.equal(tf.argmax(finalOutput,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

