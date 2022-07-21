import matplotlib.pyplot as plt

def function1(num):
    total = 0
    for i in range(1,num+1):
        temp = ((-1)**(i+1))/i
        total += temp
    return total


print(function1(193))

def loopf(f,x):
    arrayy = []
    for i in range(len(x)):
        arrayy.append(f(x[i]))
    return arrayy

xplot = list(range(1,100))

print(xplot)

plt.plot(xplot,loopf(function1,xplot))
plt.show()