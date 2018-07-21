import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 生成随机1000个点，围绕 y=0.1x + 0.3的附近
num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0,0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1,y1])

# 生成一些样本
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# 画图
plt.scatter(x_data,y_data,c='r')
plt.show()

# 生成1维的W矩阵，取值[-1,1]的一个随机数
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name = 'W')
# 生成1维的b矩阵，初始值0
b = tf.Variable(tf.zeros([1]))
# 预估值y
y = W * x_data + b

