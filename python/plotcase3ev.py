import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1500.153015607592, 1504.7338928268332, 1552.4462931204896, 1771.793003179714, 2337.8766579059957, 3338.6360802892405, 4769.016328156114, 7011.560693641619, 8636.363636363636]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Expected Value in $USD')
plt.title('Expected Value for each possible option (with exactly 3 balls matching)')
plt.bar(x,y)
plt.show()