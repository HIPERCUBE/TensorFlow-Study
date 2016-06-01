import tensorflow as tf

# Basic constant operations
# The value returned by the constructor represents the output of the Constant op.
a = tf.constant(2)
b = tf.constant(3)

# Launch the default graph.
with tf.Session() as sess:
    print "a=2, b=3"
    print "Addition with constants: %i" % sess.run(a + b)
    print "Multiplication with constants: %i" % sess.run(a * b)