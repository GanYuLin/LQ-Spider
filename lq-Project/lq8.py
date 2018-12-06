'''
基础数据类型 运算符 流程 字典 数组
四则运算
'''

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 两个常量
data1 = tf.constant(6)
data2 = tf.constant(2)

# 定义一个加法操作
dataAdd = tf.add(data1,data2)
# 定义一个乘法操作
dataMul = tf.multiply(data1,data2)
# 定义一个减法操作
dataSub = tf.subtract(data1,data2)
# 定义一个除法操作
dataDiv = tf.divide(data1,data2)

# 使用sess创建。with不需要close
with tf.Session() as sess:
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
print('end!')

















