import numpy as np
from numpy import random
x = np.array([["Jay","Ketul","Jimmy","Gohil"],[10,5,16,50]])
y = np.array([["Dhaval","Jenil","Kishan","Amit"],[29,58,45,102]])
x = np.concatenate((x,y),axis=1)
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
resparr = x.reshape(2,2,4)
print()
print("Reshaped Into 3-d:\n",resparr)
print()
for idx,elem in np.ndenumerate(x[0]):
    print(elem,"=",x[1,idx[0]])
print()
jp = np.where(x=="Jay")
print("Roll Number of Jay:",x[1,jp[1][0]]) 
print()
print("Full Sorted Array:\n",np.sort(x))
filter_arr = []

for item in x[1]:
    if int(item) > 30:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = x[1,filter_arr]
np_arr = np.array(filter_arr)
new_index = np.where(np_arr==True)
print()
print("Roll Number Greater Than 30:")
print(x[0,new_index[0]],"=",new_arr)
print()
print("Lucky Winner:",random.choice(x[0]))