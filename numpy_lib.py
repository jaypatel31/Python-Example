import numpy as np

x = np.array([["Jay","Ketul","Jimmy","Gohil"],[10,5,16,50]])

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
cparr = x.copy()#Copy Of Array x
vwarr = x.view()#View Of Array x
print() 
print("Shape of Array:",x.shape)#Number of Element Present In Each Dimensons
resparr = x.reshape(2,2,2)
print()
print("Reshaped Into 3-d:\n",resparr)
print()
for idx,elem in np.ndenumerate(x[0]):
    print(elem,"=",x[1,idx[0]]) 