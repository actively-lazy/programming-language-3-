import random


def fun1():
    list1 = []
    for i in range(0, 10):
        list1.append(i)
    print(list1)
    list2 = list1.copy()
    for i in range(5, 10):
        list2.insert(i, i * 10)
    print(list2)
    list1.extend(list2)
    print(list1)
    print(list1.sort())


def fun2():
    list1 = []
    for i in range(0, 20):
        list1.insert(i, random.randint(0, 100))
    print(list1)
    list1.sort()
    print("second smallest = ", list1[1])
    print("second largest = ", list1[len(list1) - 2])


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
    for i in range(1, 100):
        list1.append(random.sample(range(0, 10), 3))
        list2.append(random.sample(range(0, 10), 3))
    print(list1)
    print(list2)
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    print(list3)


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
    list1 = []
    for arg in args:
        list1.append(arg)
    return args


def fun7():
    str = input("Enter String: ")
    str = str.split(" ")
    print(str)
    str.sort()
    print(str)
    list1 = []
    list2 = []
    prevword = str[0]
    for word in str:
        if (word[0] == prevword[0]):
            list2.append(word)
        else:
            list1.append(list2)
            list2 = []
            list2.append(word)
        prevword = word
    list1.append(list2)
    print(list1)


fun1()
fun2()
fun3()
# fun4()
fun5()
print(fun6('a', 'b', 'c', 1, 2, 3))
fun7()
