'''
矩阵相乘
'''


import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 两行三列零矩阵
mat0 = tf.constant([[0,0,0],[0,0,0]])

# 两行三列零矩阵
mat1 = tf.zeros([2,3])

# 三行两列一矩阵
mat2 = tf.ones([3,2])

# 两行三列填充矩阵(15)
mat3 = tf.fill([2,3],15)
with tf.Session() as sess:
    print(sess.run(mat0))
    print('************')
    print(sess.run(mat1))
    print('************')
    print(sess.run(mat2))
    print('************')
    print(sess.run(mat3))






