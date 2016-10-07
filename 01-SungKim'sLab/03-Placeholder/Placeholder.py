import tensorflow as tf

# Start tf Session

sess = tf.Session()

# Basic Operations with variable as graph input
# The value returned by the constructor represents the output
# of the Variable op. (define as input when running session)
# tf Graph input
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

# Define some operations
add = tf.add(a, b)
mul = tf.mul(a, b)

# Launch the default graph.
with tf.Session() as sess:
    print "a=2, b=3"
    print "Addition with constants: %i" % sess.run(add, feed_dict={a: 2, b: 3})
    print "Multiplication with constants: %i" % sess.run(mul, feed_dict={a: 2, b: 3})
