import random

inputPath = input("Enter the path of file u want to open");
f1 = open(inputPath, 'r')
print(f1.read())
outputPath = input("Enter the path of file u want to create ")
f2 = open(outputPath, 'w')
text = input("Enter text you want to add")
f2.write(text)
f1.close()
f2.close()
fromPath = input("Enter the path of file u want to copy from");
toPath = input("Enter the path of file u want to copy to");
print("copied from ", fromPath, " to ", toPath)
with open(fromPath) as f:
    lines = f.readlines()
    lines = [l for l in lines]
    with open(toPath, "w") as f1:
        f1.writelines(lines)

n1 = float(input("Enter number 1"))
n2 = float(input("Enter number 2"))
try:
    print("Division of both numbers are", (n1 / n2))
except Exception as e:
    print("Not possible to divide, sry")
    print("Error = ", str(e))
arr = []
for i in range(int(input("Enter the size of array you want to create"))):
    arr.append(random.randint(0, 100))
print(arr)

index = int(input("Enter position of index"))
try:
    print(arr[index])
except Exception as  e:
    print("Error occurred, sry")
    print("Error = ", str(e))


class EmailError(Exception):
    def __str__(self):
        return "Email Error called"


email = input("Enter email address")
try:
    count = 0
    for e in email:
        if e == "." or e == "@":
            count += 1
    if (count > 2):
        raise EmailError
except EmailError as e:
    print("Email error")
    print("Error =  ", str(e))


class AgeError(Exception):
    def __str__(self):
        return "Age Error called"

age = int(input("Enter age"))
try:
    if not (15 <= age <= 80):
        raise AgeError
except AgeError as e:
    print("Age error")
    print("Error =  ", str(e))
