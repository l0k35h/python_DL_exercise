import numpy as np
a=np.arange(15)
#it will print as list
print(a)
a=np.arange(15).reshape(3,5)
#after writing reshape it will print in array format
print(a)
#print shape and other numpy attributes
print(a.shape)
# 3,5
print(a.ndim)
# 2
print(a.dtype.name)
# int32
print(a.itemsize)
# 4
print(a.size)
# 15
