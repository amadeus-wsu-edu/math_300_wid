from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

evaldiff = diff(x**3 - ((cos(pi * x)**2)/2*(x**2)+1)+(11*x*x/3)-1,x)
pprint(evaldiff)