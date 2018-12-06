import tensorflow as s
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

s1 = s.constant("hello tensorflow")
sess=s.Session()
print(sess.run(s1))






