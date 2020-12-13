from scipy import constants
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

print("1 year =",constants.year,"s")#Return in Seconds
print("1 centimeter =",constants.centi,"m")#Return in Meter
print("1 KB =",constants.kibi,"Bytes")
print("1 Bar =",constants.bar,"Pascal")  
print("1 km/s =",constants.kmh,"m/s") 
print("1 eV =",constants.eV,"Joules")
print("1 HP =",constants.hp,"Watt") 
print("1 Dyne =",constants.dyn,"Newton")

arr = np.array([[0, 0, 0, 2], [0, 0, 1, 0], [1, 0, 2,0]])

print(csr_matrix(arr))
print()
print("Non - Zero Data:",csr_matrix(arr).data)
print()
print("Total Non - Zero Data:",csr_matrix(arr).count_nonzero())
arr2 = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

gp = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr2)
gpcsr = csr_matrix(gp)
print()
print(dijkstra(newarr, return_predecessors=True, indices=0))
print()
print(depth_first_order(gpcsr, 3))