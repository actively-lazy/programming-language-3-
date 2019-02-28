def printMenu():
    print("Menu")
    print("1){}\n2){}\n3){}\n4){}\n5){}\n".format(
        "Insert", "Remove", "Update", "Print", "Exit"))


def inputRollno():
    rollno = input("Roll no")
    try:
        rollno = int(rollno)
    except Exception as e:
        rollno = -1
    return rollno


def inputname():
    return input("Enter name: ")


def insert():
    roll = inputRollno()
    if roll in student:
        print("Student already present with roll no %d" % (roll))
    else:
        name = inputname()
        student[roll] = name


def update():
    roll = inputRollno()
    if roll not in student:
        print("Student not present with roll no %d" % (roll))
    else:
        name = inputname()
        student[roll] = name


def remove():
    roll = inputRollno()
    if roll not in student:
        print("Student not present with roll no %d" % (roll))
    else:
        name = student[roll]
        student.pop(roll)
        print("Student with roll no %d and name %s deleted" % (roll, name))


def printstudents():
    print("{:<7}        {:<10}".format("Roll no", "Name"))
    for k, v in student.items():
        print("{:<7}{:<10}".format(k, v))


student = dict()

while True:
    printMenu()
    try:
        choice = int(input("Enter choice"))
    except Exception as e:
        print("Invalid choice")
        continue
    if(choice == 1):
        insert()
    if(choice == 2):
        remove()
        continue
    if(choice == 3):
        update()
        continue
    if(choice == 4):
        printstudents()
        continue
    if(choice == 5):
        break

print("Students = ", student)
printstudents()
