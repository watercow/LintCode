from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets('data/', one_hot = True)

# 参数设置
numClasses = 10
inputSize = 784
trainingIterations = 50000
batchSize = 64

# 指定x和y的大小
X = tf.placeholder(tf.float32, shape = [None, inputSize])
y = tf.placeholder(tf.float32, shape = [None, numClasses])

# 参数初始化
W1 = tf.Variable(tf.random_normal([inputSize, numClasses], stddev=0.1))
B1 = tf.Variable(tf.constant(0.1), [numClasses]) # b和输出结果的维数一一对应

# 构造模型
y_pred = tf.nn.softmax(tf.matmul(X,W1) + B1)

loss = tf.reduce_mean(tf.square(y - y_pred))
opt = tf.train.GradientDescentOptimizer(learning_rate= .05).minimize(loss)

correct_prediction = tf.equal(tf.argmax(y_pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

# 迭代计算
for i in range(trainingIterations):
    batch = mnist.train.next_batch(batchSize)
    batchInput = batch[0]
    batchLabels = batch[1]
    _,trainingLoss = sess.run([opt, loss], feed_dict={X: batchInput, y: batchLabels})
    if i % 1000 ==0 :
        train_accuracy = accuracy.eval(session = sess, feed_dict={X: batchInput, y: batchLabels})
        print("step %d , training acc %g" % (i,train_accuracy))

# 测试结果
batch = mnist.test.next_batch(batchSize)
testAccuracy = sess.run(accuracy, feed_dict={X:batch[0],y:batch[1]})
print("test accuracy %g" % (testAccuracy))