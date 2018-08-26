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

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(trainingIterations):
    batch = mnist.train.next_batch(batchSize)
    batchInput = batch[0]
    batchLabels = batch[1]
    _, trainingLoss = sess.run([opt, loss],feed_dict={X:batchInput, y:batchLabels})
    if i%1000 == 0:
        trainAccuracy = accuracy.eval(session=sess,feed_dict={X:batchInput, y:batchLabels})
        print("step %d, training accuracy %g" % (i, trainAccuracy))

# 之前是单层的神经网络
# 如果要变成两层的神经网络
# 第一个隐藏50个神经元 第二个隐层100个神经元，输入输出层不变
numHiddenUnitsLayer2 = 100
# 参数初始化应变为
W1 = tf.Variable(tf.truncated_normal([inputSize, numHiddenUnits], stddev = 0.1))
B1 = tf.Variable(tf.constant(0.1), [numHiddenUnits])
W2 = tf.Variable(tf.truncated_normal([numHiddenUnits, numHiddenUnitsLayer2], stddev = 0.1))
B2 = tf.Variable(tf.constant(0.1), [numHiddenUnitsLayer2])
W3 = tf.Variable(tf.random_normal([numHiddenUnitsLayer2, numClasses], stddev = 0.1))
B3 = tf.Variable(tf.constant(0.1), [numClasses])

# 网络结构应变为
hiddenLayerOutput = tf.matmul(X,W1) + B1
hiddenLayerOutput = tf.nn.relu(hiddenLayerOutput)
hiddenLayer2Output = tf.matmul(hiddenLayerOutput, W2) + B2
hiddenLayer2Output = tf.nn.relu(hiddenLayer2Output)
finalOutput = tf.matmul(hiddenLayer2Output, W3) + B3

#其余部分无需变化