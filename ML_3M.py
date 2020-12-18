import numpy as np
from scipy import stats

marks = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("Average Marks:",np.mean(marks))

print("Middle Marks:",np.median(marks))

md = stats.mode(marks)
print("Most Appeared Marks:",md.mode[0])