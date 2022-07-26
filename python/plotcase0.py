import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [99.807, 96.746, 81.068, 46.6, 13.788, 1.387, 0.0, 0.0, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Probability in %')
plt.title('Probabilities for each possible option (with exactly 0 balls matching)')
plt.bar(x,y)
plt.show()


