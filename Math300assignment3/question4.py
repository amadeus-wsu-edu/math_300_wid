def midpoint(f,a,b,n):
    total = 0
    h = (b-a)/n
    for i in range(0,n):
        total += f(((a+(i*h)+(i+1)*h)/2)*h)
    return total

functionlambda = lambda a : a**a


#def midpointplot(f,a=0,b=1,n=100):