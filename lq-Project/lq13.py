


import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 三行一列的矩阵
mat1 = tf.constant([[2],[3],[4]])
# 与mat1具有相同的维度，但mat2内容为0
mat2 = tf.zeros_like(mat1)

# 将0-2之间数据分成相等的10份，中间有10个数据，要填11
mat3 = tf.linspace(0.0,2.0,11)

# 随机数矩阵，2行三列，数字为-1到2之间的随机数
mat4 = tf.random_uniform([2,3],-1,2)


with tf.Session() as sess:
    print(sess.run(mat2))
    print('************')
    print(sess.run(mat3))
    print('************')
    print(sess.run(mat4))
