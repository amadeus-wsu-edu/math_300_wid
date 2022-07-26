import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [100.0, 100.0, 99.059, 89.328, 59.138000000000005, 21.987000000000002, 3.427, 0.13799999999999998, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Probability in %')
plt.title('Probabilities for each possible option (with exactly 2 balls matching)')
plt.bar(x,y)
plt.show()
