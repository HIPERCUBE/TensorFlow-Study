import tensorflow as tf

# Start tf Session

sess = tf.Session()

# Basic constant operations
# The value returned by the constructor represents the output
# of the Constant op
a = tf.constant(2)
b = tf.constant(3)

c = a + b

# Print out operation
print(c)

# Print out the result of operation
print(sess.run(c))

# Launch the default graph.
with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition with constants: %i" % sess.run(a + b))
    print("Multiplication with constants: %i" % sess.run(a * b))
