import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1497.2577202874693, 1455.769851954248, 1258.5371609069184, 844.7813901548526, 395.03239410793964, 103.75264929559906, 0.0, 0.0, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Expected Value in $USD')
plt.title('Expected Value for each possible option (with exactly 0 balls matching)')
plt.bar(x,y)
plt.show()