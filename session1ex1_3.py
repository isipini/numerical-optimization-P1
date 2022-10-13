# ik krijg in een type error message

from cvxopt import matrix, solvers

P = 2*matrix([3])

q = matrix([-2])

G =  matrix([2])

h = matrix([-7])


sol=solvers.qp(P, q, G, h)
