import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant operation
# The op(operation) added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.

hello = tf.constant('Hello, TensorFlow!')

print hello

# Start tf session
sess = tf.Session()

print(sess.run(hello))
