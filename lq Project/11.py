'''
矩阵相乘
矩阵输出
'''



import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
                     [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])

# 矩阵相乘
matMul = tf.matmul(data1, data2)

# 直接使用简单乘法，对应元素相乘
matMul2 = tf.multiply(data1, data2)

# 矩阵相加
matAdd = tf.add(data1, data3)

with tf.Session() as sess:
    print(sess.run(matMul))  # data1 [[6, 6]] 乘以 data2 [[2],
                                                    #    [2]] 得到结果值24
    print("--------")
    print(sess.run(matAdd))  # 1行2列 加 1行2列 还是一行两列
    print("--------")
    print(sess.run(matMul2))  # 1x2 2x1 = 2x2 这里涉及到python的广播机制
    print("--------")
    # [6,6] 和 [[2].[2]] 都会被补全成一个2x2的矩阵。然后对应元素相乘

    # 使用print一次打印多个内容
    print(sess.run([matMul, matAdd]))
