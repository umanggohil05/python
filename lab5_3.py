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


list3()
