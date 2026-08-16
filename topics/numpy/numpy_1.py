import numpy
import matplotlib.pyplot as plt


list_1 = [1, 2, 3, 4, 5]
array_1 = numpy.array([[1, 2, 3], [4, 5, 6]], numpy.int32)
print(f"list_1 = {list_1}")

print(f"array_1 = {array_1}")
print(f"array_1 shape = {array_1.shape}")
print(f"array_1 (1, 2): {array_1[1, 2]}")
array_1[1, 2] = 100
print(f"array_1 = {array_1}")
print(f"array_1 (1, 2): {array_1[1, 2]}")
