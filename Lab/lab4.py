import random
daysOfTheWeek = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
name = ""
first_names = ('John', 'Andy', 'Joe')
last_names = ('Johnson', 'Smith', 'Williams')
group = []
for i in range(10):
    full_name = random.choice(first_names) + " " + random.choice(last_names)
    group.append(full_name)
print("Group = ", group)
namesOfStudent = set()
# while (True):
#     name = input("Enter name of student:\n")
#     if name == "#":
#         break
#     else:
#         namesOfStudent.add(name)
namesOfStudent = set(group)
print("Student = ", namesOfStudent)
attendanceStudents = {}
currattendence = []
for name in namesOfStudent:
    print("Enter Attendance % for ", name)
    for day in daysOfTheWeek:
        # print("Enter Attendance for ", day)
        # currattendence.append(int(input()))
        randomInteger = random.randint(0, 100)
        currattendence.append(randomInteger)
    print(currattendence)
    attendanceStudents[name] = currattendence.copy()
    currattendence.clear()
print(attendanceStudents)

for student in attendanceStudents.keys():
    avg = 0
    attendance = attendanceStudents[student]
    for a in attendance:
        avg += int(a)
    avg = avg / 7
    print("avg attendance for ", student, " {0} = {1} ".format(attendance,int(avg)))
