import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [100.0, 99.53999999999999, 93.99499999999999, 71.55, 33.947, 7.595000000000001, 0.5499999999999999, 0.0, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Probability in %')
plt.title('Probabilities for each possible option (with exactly 1 balls matching)')
plt.bar(x,y)
plt.show()
