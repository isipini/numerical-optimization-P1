from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt
c = np.array([1, 1])
bounds = [[0,0],[None,None]]
Aub = np.matrix([[4,-1],[2,1],[-5,2]])
bub = np.array([8,10,2])
res = linprog(c = c, bounds =bounds,A_ub = Aub,b_ub = bub)
print(res.fun)
