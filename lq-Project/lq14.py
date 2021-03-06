import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 利用np生成100个随机点
x_data=np.random.rand(100)
y_data=x_data*0.1+0.2

# 构造一个线性模型

b=tf.Variable(1.1)
k=tf.Variable(0.5)
y=k*x_data+b


# 二次代价函数
loss=tf.reduce_mean(tf.square(y_data-y))
# 定义一个梯度下降法来进行优化的训练的优化器
optimizer=tf.train.GradientDescentOptimizer(0.2)
# 最小化代价函数
train=optimizer.minimize(loss)
# 初始化变量
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(421):
        sess.run(train)
        # 每20次输出一次
        if step%20==0:
            print(step,sess.run([k,b]))









