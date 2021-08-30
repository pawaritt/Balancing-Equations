import numpy as np
# A = np.array([[1, 0, 1, 0, 0, -2],
#               [1, 2, 1, -3, -2, 0],
#               [0, 0, 1, -1, -1, 0],
#               [0, 1, 0, -1, 0, 0],
#               [3, 0, 0, 0, 0, -1]])
# B = np.array([0, 0, 0, 0, 0])
# #
# # sol = np.linalg.lstsq(A, b)
# # print(sol)
#
# print(np.linalg.solve(A, B))
# import numpy as np

a = np.array([[1, 0, 0, 0], [0, 1, -4, 0], [0, 0, -3, 0], [0, 2, 0, -2]])
b = np.array([1, 0, -1, 0])
x = np.linalg.solve(a, b)
print(x)

