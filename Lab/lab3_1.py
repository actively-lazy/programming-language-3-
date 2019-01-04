import random
def fun1():
    list1 = []
    for i in range(0,10):
        list1.append(i)
    print(list1)
    list2 = list1.copy()
    for i in range(5,10):
        list2.insert(i,i*10)
    print(list2)
    list1.extend(list2)
    print(list1)
    print(list1.sort())

def fun2():
    list1 = []
    for i in range(0,20):
        list1.insert(i,random.randint(0,100))
    print(list1)
    list1.sort()
    print("second smallest = ", list1[1])
    print("second largest = ", list1[len(list1)-2])
def fun3():
    list1 = []
    list2 = []
    for i in range(0, 20):
        list1.insert(i, random.randint(0, 10))
        list2.insert(i, random.randint(0, 10))
    print(list1)
    print(list2)
    print(set(list1).intersection(set(list2)))
    list1 = []
    list2 = []
    for i in range(1,100):
        list1.append(random.sample(range(0,10),3))
        list2.append(random.sample(range(0,10),3))
    print(list1)
    print(list2)
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    print(list3)
