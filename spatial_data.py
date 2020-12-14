import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# Find Distance between two points

p1 = (1, 0)
p2 = (1, 4)

res = euclidean(p1, p2)

print("Distance Between (1,0) and (1,4)",res)

# In this we have to calculate distance by moving either top, bottom, left, right

p3 = (1, 0)
p4 = (10, 2)

res2 = cityblock(p3, p4)

print("Distance Between (1,0) and (10,2) By Cityblock",res2)