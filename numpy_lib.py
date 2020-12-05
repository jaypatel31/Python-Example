import numpy as np

x = np.array([["Jay","Ketul","Jimmy"],[10,5,16]])

print("Array:\n",x)
print("Array is",x.ndim,"dimensions")
print()
print()
print("Name = Roll Number")
print()
print(x[0,0],"=",x[1,0].astype('f'))
print()
print()
print("{Name} = {Roll Number}")
print()
print("{",x[0,1:],"}","=","{",x[1,1:],"}")
print()
print("Data Type Of Array",x.dtype)