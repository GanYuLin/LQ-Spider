'''
基础数据类型 运算符 流程 字典 数组
四则运算
'''


import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data1 = tf.constant(6)
# data2变量
data2 = tf.Variable(2)
dataAdd = tf.add(data1, data2)

# 完成当前的数据拷贝: 把当前dataAdd的结果追加到data2中
dataCopy = tf.assign(data2, dataAdd)  # dataAdd ->data2

dataMul = tf.multiply(data1, data2)
dataSub = tf.subtract(data1, data2)
dataDiv = tf.divide(data1, data2)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))

    # 将6和2相加的结果放到data2中
    print('sess.run(dataCopy)', sess.run(dataCopy))  # 8->data2

    # 除过run方法还可以使用.eval()直接输出。eval方法相当于下面这句话
    print('dataCopy.eval()', dataCopy.eval())  # 8+6->14->data2 = 14

    # 获取默认的session，执行run操作
    print('tf.get_default_session()', tf.get_default_session().run(dataCopy))
print('end!')

