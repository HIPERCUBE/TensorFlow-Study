import tensorflow as tf

# Simple hello word using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
# The Value returned by constructor represents the output of the Constant op.
hello = tf.constant('Hello, TensorFlow')

# Print Tensor info
print hello

# Start tf session
sess = tf.Session()

print sess.run(hello)