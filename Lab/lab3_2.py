import random

# def fun4():
def fun5():
    list1 = []
    for i in range(1, 20):
        list1.append(i)
    print(list1)
    random.shuffle(list1)
    print(list1)
    list1 = []
    list2 = []
    list3 = []
    for i in range(1, 10):
        list1.insert(i, random.randint(0, 10))
        list2.insert(i, random.randint(0, 10))
        list3.insert(i, random.randint(0, 10))
    print(list1)
    print(list2)
    print(list3)
    print(set(zip(list1, list2, list3)))
def fun6(*args):
    list1= []
    for arg in args:
        list1.append(arg)
    return args
def fun7():
    str = input("Enter String: ")
    str = str.split(" ")
    print(str)
    str.sort()
    print(str)

