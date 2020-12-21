import numpy as np

marks = [99,86,87,88,86,87,94,78,77,85,86]

x = np.percentile(marks,80)

print("80% student has scored",x,"and Above marks.")
