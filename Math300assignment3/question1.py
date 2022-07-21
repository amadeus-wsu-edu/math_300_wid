import numpy as np

amatrix = np.array([[1,2],[3,4]])
bmatrix = np.array([[5],[8]])
from scipy import linalg
xmatrix = linalg.solve(amatrix,bmatrix)
print(xmatrix)








