'''
打印矩阵
[[6,6]] 一行两列的矩阵

'''




import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 一行两列矩阵
data1 = tf.constant([[6, 6]])
# 两行一列矩阵
data2 = tf.constant([[2],
                     [2]])
# 一行两列
data3 = tf.constant([[3, 3]])
# 三行两列
data4 = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])

print(data4.shape)  # 打印矩阵的维度
print("--------")

with tf.Session() as sess:
    print(sess.run(data4))  # 打印整体
    print("-------")
    print(sess.run(data4[0]))  # 打印某一行
    print("---------")
    print(sess.run(data4[:, 0]))  # M*N的矩阵，第一位是行，第二位是列。
    # 打印某一列，使用:表示所有行
    print("-------")
    print(sess.run(data4[0, 1]))  # 1 1  下标从0开始算。但是shape是从1开始算的
