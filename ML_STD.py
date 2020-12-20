import numpy as np

marks = [99,86,87,88,86,87,94,78,77,85,86]

x = np.std(marks)
y = np.var(marks)
print("Standard Deviation:",x)
print("Variance:",y)
if x<=2:
    print("Excellent Perfomance Class.")
elif x<=6:
    print("Good Perfomance Class.")
else:
    print("Need Improvement Class.")
