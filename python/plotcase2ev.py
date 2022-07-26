import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1500.153015607592, 1504.7338928268332, 1537.8377735022257, 1619.3697858316025, 1694.3302670985881, 1644.7076424385987, 1364.7949024293114, 797.6878612716763, 0.0]

plt.xticks(range(len(x)+1))
plt.xlabel('At least \'X\' number of matches')
plt.ylabel('Expected Value in $USD')
plt.title('Expected Value for each possible option (with exactly 2 balls matching)')
plt.bar(x,y)
plt.show()