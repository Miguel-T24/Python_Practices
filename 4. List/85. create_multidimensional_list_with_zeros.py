# 85. Writea multidimensional list (list of list) with zeros

# Normal
result = [[0,0] for i in range(3)]
print(result)

# With numpy
import numpy as np
print(np.zeros((3,2), int))