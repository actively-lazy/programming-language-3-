import random


def q1():
    while (True):
        rand = random.randrange(1, 10)
        guess = int(input("Enter your guess: "))
        if rand == guess:
            print("Yes!!!! \nRandom was ", rand)
            break
        else:
            print("The random number was = ", rand)


def q2():
    x = input("x: ")
    y = input("y: ")
    z = input("z: ")
    if x == y == z:
        print("equilateral triangle")
    elif x != y and y != z and z != x:
        print("scalene triangle")
    else:
        print("isosceles triangle")


def q3(num):
    for i in range(1, 101):
        print("{:<3}x{:^6}={:>5}".format(num, i, num * i))


def q4():
    toss = random.randrange(0, 2)
    return toss


for i in range(2, 10000):
    count = i
    result = list()
    for i in range(0, count):
        result.append(q4())

    head, tail = 0, 0
    for r in result:
        if r == 1:
            head += 1
        else:
            tail += 1
    headdiff = 50 - (head / count)*100
    taildiff = 50 - (tail / count)*100
    if abs(headdiff) + abs(taildiff) <2:
        print("{:7} Experiments {:7} Head {:7} Tail {:7.3f},{:7.3f}  {:5.0f}".format(count, head, tail, headdiff, taildiff,
                                                                                 abs(headdiff) + abs(taildiff)))
