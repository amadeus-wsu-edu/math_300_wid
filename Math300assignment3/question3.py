import matplotlib.pyplot as plt

def function2(x,num):
    total = 0
    for i in range(1,num+1):
        temp = (x**i)/i
        total += temp
    return total

def loopf(f,x):
    arrayy = []
    for i in range(len(x)):
        arrayy.append(f(x[i],50))
    return arrayy

xplot = list(range(1,100))
plt.plot(xplot,loopf(function2,xplot))
plt.show()
