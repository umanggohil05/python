import random
def GenRand() :
    oddlist = []
    for i in range (5):
        x=random.randint(1,100)*2-1
        oddlist.append(x)
        print(x)
    print(oddlist)
    oddlist2=[random.randint(1,100)*2-1 for x in range (1,6)]
    evenlist=[random.randint (1,100)*2 for x in range (4) ]
    print(oddlist2,evenlist)
    oddlist2.pop(2)
    oddlist2.insert(2,evenlist)
    print(oddlist2)
    finalList =[]
    for x in oddlist2:
        if type(x) == list:
            finalList.extend(x)
        else:
            finalList.append(x)
        print(finalList)
        finalList.sort()
        print(finalList)
        finalList.sort(reverse=True)
        print(finalList)
GenRand()
