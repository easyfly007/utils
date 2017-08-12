import tensorflow as tf 
features = tf.placeholder(dtype = tf.float32, shape = [None, 28*28], name = 'feature_1')
labels = tf.placeholder(dtype = tf.float32, shape = [None, 10], name = 'labels_1')
w = tf.Variable(tf.truncated_normal([28*28, 10]))
w = tf.Variable(tf.random_normal([28,10]))
print('end')