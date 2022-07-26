import random

def simulation(value, num, slist):
    random.seed(123)
    successcounter = 0
    totalcount = 0
    while totalcount != value:
        totalcount += 1
        templista = slist.copy()
        templistb = slist.copy()
        handa = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        handb = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            handa[i] = templista.pop(random.randint(0, len(templista) - 1))
            handb[i] = templistb.pop(random.randint(0, len(templistb) - 1))
        similaritylist = list(set(handa).intersection(set(handb)))
        #print(similaritylist)
        #print(handa)
        #print(handb)
        if len(similaritylist) > 0:
            count = 0
            for j in range(len(similaritylist)):
                numa = handa.count(similaritylist[j])
                numb = handb.count(similaritylist[j])
                #print(min(numa,numb))
                count += min(numa,numb)
            if count >= num:
                successcounter += 1

    return successcounter

slist1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]



def loopsim(value, num, slist):
    count = 1
    probarray = []
    while num >= count:
        probarray.append(simulation(value, count, slist))
        count += 1
    return probarray

def probabilitylist(arraya, num):
    arrayb = []
    for i in range(len(arraya)):
        arrayb.append((arraya[i]/num)*100)
    return arrayb

def expectedvaluelist(arraya, prize):
    arrayb = []
    for i in range(len(arraya)):
        arrayb.append(prize/(arraya[i]/100))
    return arrayb

#print(loopsim(1000000, 9, slist1))
#with a seed of 123 and a sample size of 1000000
#[999898, 996854, 966217, 827433, 523552, 200525, 37665, 2595, 33]
# 1       2       3       4       5       6       7      8     9
plist = probabilitylist([999898, 996854, 966217, 827433, 523552, 200525, 37665, 2595, 33],1000000)
print(plist)
#[99.9898, 99.6854, 96.6217, 82.74329999999999, 52.3552, 20.052500000000002, 3.7664999999999997, 0.2595, 0.0033000000000000004]

#I want the expected value to be $1500
# x * probability = $1500
# x = 1500/probability

evlist = expectedvaluelist(plist,1500)
print(evlist)
#for expected value of $1500
#[1500.153015607592, 1504.7338928268332, 1552.4462931204896, 1812.8356011906708, 2865.044923904407, 7480.364044383493, 39824.77100756671, 578034.6820809249, 45454545.45454545]

#get unique list of balls from handa
#randomly pick 3 balls into an array
#compare that array with handb and see how many match

def revealed(handa, handb, revealsize):
    uniquea = list(set(handa.copy()))
    reveallist = []
    for i in range(revealsize):
        reveallist.append(uniquea.pop(random.randint(0, len(uniquea) - 1)))
    similaritylist = list(set(reveallist).intersection(set(handb)))
    return len(similaritylist)

#revealsize = number of balls shown
#revealnum = number of balls matching
def simulation2(value, num, slist, revealsize, revealnummatch):
    random.seed(123)
    successcounter = 0
    totalcount = 0
    while totalcount != value:
        templista = slist.copy()
        templistb = slist.copy()
        handa = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        handb = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            handa[i] = templista.pop(random.randint(0, len(templista) - 1))
            handb[i] = templistb.pop(random.randint(0, len(templistb) - 1))
        if revealed(handa, handb, revealsize) == revealnummatch:
            totalcount += 1
            similaritylist = list(set(handa).intersection(set(handb)))
            if len(similaritylist) > 0:
                count = 0
                for j in range(len(similaritylist)):
                    numa = handa.count(similaritylist[j])
                    numb = handb.count(similaritylist[j])
                    #print(min(numa,numb))
                    count += min(numa,numb)
                if count >= num:
                    successcounter += 1
    return successcounter

def loopsim2(value, num, slist, revealsize, revealnummatch):
    count = 1
    probarray = []
    while num >= count:
        probarray.append(simulation2(value, count, slist, revealsize, revealnummatch))
        count += 1
    return probarray

def newexpectedvalue(arraya, prizearray):
    arrayb = []
    for i in range(len(arraya)):
        arrayb.append(prizearray[i] * (arraya[i] / 100))
    return arrayb

print ('new ev lists')

#case0revealed = loopsim2(100000, 9, slist1, 3, 0)
#print(case0revealed)
#[99807, 96746, 81068, 46600, 13788, 1387, 0, 0, 0]
plist0 = probabilitylist([99807, 96746, 81068, 46600, 13788, 1387, 0, 0, 0],100000)
print(plist0)

ev0 = newexpectedvalue(plist0, evlist)
print(ev0)
#case1revealed = loopsim2(100000, 9, slist1, 3, 1)
#print(case1revealed)
#[100000, 99540, 93995, 71550, 33947, 7595, 550, 0, 0]
plist1 = probabilitylist([100000, 99540, 93995, 71550, 33947, 7595, 550, 0, 0],100000)
print(plist1)

ev1 = newexpectedvalue(plist1, evlist)
print(ev1)


#case2revealed = loopsim2(100000, 9, slist1, 3, 2)
#print(case2revealed)
#[100000, 100000, 99059, 89328, 59138, 21987, 3427, 138, 0]
plist2 = probabilitylist([100000, 100000, 99059, 89328, 59138, 21987, 3427, 138, 0],100000)
print(plist2)

ev2 = newexpectedvalue(plist2, evlist)
print(ev2)

#case3revealed = loopsim2(100000, 9, slist1, 3, 3)
#print(case3revealed)
#[100000, 100000, 100000, 97736, 81600, 44632, 11975, 1213, 19]
plist3 = probabilitylist([100000, 100000, 100000, 97736, 81600, 44632, 11975, 1213, 19],100000)
print(plist3)

ev3 = newexpectedvalue(plist3, evlist)
print(ev3)