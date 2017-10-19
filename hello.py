import tensorflow as tf
hello = tf.constante('Hello, Tensorflow.')
sess = tf.Session()
print(sess.run(hello))
