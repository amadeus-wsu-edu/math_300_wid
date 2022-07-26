import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [100.0, 100.0, 100.0, 97.736, 81.6, 44.632, 11.975, 1.213, 0.019]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Probability in %')
plt.title('Probabilities for each possible option (with exactly 3 balls matching)')
plt.bar(x,y)
plt.show()
