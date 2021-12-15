import numpy as np

list_data = [0, 1, 2, 3, 4, 5.0]
a1 = np.array(list_data)
print(a1)
print(type(a1))

a2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a2)

print(np.arange(0, 10, 1))

print(np.arange(0, 24, 1).reshape(2, 3, 4))