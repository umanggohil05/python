import random
def list3():
    lst = [random.randint(1,30) for x in range (50)]
    print(lst)
    for x in lst:
        c= lst.count(x)
        if c >= 2:
            for y in range (c-1):
                lst.remove(x)
                print("removed",x)
    print(lst)


#list3()
def list4():
    lst = [random.randint(-200,200) for x in range(30)]
    print(lst)
    plst = []
    nlst = []
    for x in lst:
        plst.append(x) if x > 0 else nlst.append(x)
    print(plst)
    print(nlst)
list4()
