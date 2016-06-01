# Installation


## install pip
``` shell
# Ubuntu/Linux 64-bit
$ sudo apt-get install python-pip python-dev

# Mac OS X
$ sudo easy_install pip
```


## install TensorFlow
``` shell
# Ubuntu/Linux 64-bit, CPU only:
$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled. Requires CUDA toolkit 7.5 and CuDNN v4.  For
# other versions, see "Install from sources" below.
$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl

# Mac OS X, CPU only:
$ sudo easy_install --upgrade six
$ sudo pip install --upgrade https://storage.googleapis.com/tensorflow/mac/tensorflow-0.8.0-py2-none-any.whl
```


## Hello, TensorFlow
[Source](/HelloTensorFlow.py)
``` python
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
```
### Result
```
Tensor("Const:0", shape=(), dtype=string)
Hello, TensorFlow
```


## Everything is operation
[Source](/EverythingIsOperation.py)
``` python
import tensorflow as tf

# Start tf session
sess = tf.Session()

# Basic constant operations
# The value returned by the constructor represents the output ot the Constant op.
a = tf.constant(2)
b = tf.constant(3)

c = a + b

# Print out operation
print c

# Print out the result of operation
print sess.run(c)
```
### Result
```
Tensor("add:0", shape=(), dtype=int32)
5
```


## Basic operations
[Source](/BasicOperations)
``` python
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
```
### Result
```
a=2, b=3
Addition with constants: 5
Multiplication with constants: 6
```


## Reference
- https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html
- https://www.youtube.com/watch?v=cbPjsOivFOs
- https://github.com/nlintz/TensorFlow-Tutorials