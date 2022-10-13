from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt
c = np.array([2, -1])
bounds = [[2,6],[3,5]]
res = linprog(c = c, bounds =bounds)
print(res.fun)
feature_x = np.arange(0, 50, 1)
feature_y = np.arange(0, 50, 1)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
  
fig, ax = plt.subplots(1, 1)
  
Z = 2*X -Y
  
# plots contour lines
ax.contour(X, Y, Z)
plt.show()

