import time
import numpy as np

start_time = time.time()

# generate two big matrices of float32
a = np.random.rand(10000, 10000).astype(np.float32)
b = np.random.rand(10000, 10000).astype(np.float32)

test = np.matmul(a, b)

print("--- %s secondspassedin2 ---" % (time.time() - start_time))

print(test[0:10, 0:10])