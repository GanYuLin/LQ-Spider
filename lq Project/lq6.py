'''
初学opencv
'''

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


hello = tf.constant('mtianyan love tensorflow!')
sess = tf.Session()
print(sess.run(hello))
sess.close()






