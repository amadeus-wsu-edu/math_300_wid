import numpy as np
import matplotlib.pyplot as plt

amatrix = np.array([[1,2],[3,4]])
bmatrix = np.array([[5],[8]])
from scipy import linalg
xmatrix = linalg.solve(amatrix,bmatrix)
print(xmatrix)

def function1(num):
    total = 0
    for i in range(1,num+1):
        temp = ((-1)**(i+1))/i
        total += temp
    return total


print(function1(193))

plt.plot([2,3],[3,5])
plt.show()



def function2(x,num):
    total = 0
    for i in range(1,num+1):
        temp = (x**i)/i
        total += temp
    return total

print(function2(1,1))

def midpoint(f,a,b,n):
    total = 0
    h = b-a/n
    for i in range(0,n):
        total += f(((a+(i*h)+h)/2)*h)
    return total

functionlambda = lambda a : a**a


#def midpointplot(f,a=0,b=1,n=100):



from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

evaldiff = diff(x**3 - ((cos(pi * x)**2)/2*(x**2)+1)+(11*x*x/3)-1,x)
pprint(evaldiff)



