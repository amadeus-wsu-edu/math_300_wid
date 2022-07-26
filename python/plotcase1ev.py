import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1500.153015607592, 1497.8121169198298, 1459.2218932186042, 1297.083872651925, 972.5968003178292, 568.1336491709263, 219.0362405416169, 0.0, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Expected Value in $USD')
plt.title('Expected Value for each possible option (with exactly 1 balls matching)')
plt.bar(x,y)
plt.show()
