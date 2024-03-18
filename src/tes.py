import numpy as np

# Assuming cpoint is a list of 2D NumPy arrays
cpoint =[1,2,3,4]
cpoint2 = [5,6,7]

# Concatenate along the first axis
result = []
result.append(cpoint)
result.append(cpoint2)

print(result[0][0:2])