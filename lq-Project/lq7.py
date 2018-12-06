'''
基础数据类型 运算符 流程 字典 数组
'''


import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 常量，指定数据类型
data1 = tf.constant(2,dtype=tf.int32)

# 变量，指定变量名
data2 = tf.Variable(10,name='var')


print(data1)
print(data2)



init = tf.global_variables_initializer()
sess = tf.Session()
with sess:
    sess.run(init)
    print(sess.run(data1))
    print(sess.run(data2))









