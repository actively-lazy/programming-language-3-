import string
str = input("Enter String: ")
print(str[::-1])
if str==str[::-1]:
    print("palindrome")
else:
    print("not palindrome")

words = str.split(" ")
count =0
for w in words:
    for letter in w:
        if letter=='a':
            count +=1
            continue;
print("number of a= ",count)
count = 0
dict ={}
for alfabets in list(string.ascii_lowercase):
    count = 0;
    for w in words:
        for letter in w:
            if letter==alfabets:
                count +=1
    dict[alfabets] = count
print(dict)
print("{0:<15}{1:^15}{2:>15}".format("KEY","PRESENT","VALUE"))
print("---------------------------------------------------------")
for key in dict.keys():
    value = dict.get(key)
    present = "absent"
    if value>0:
        present = "present"
    print("{0:<15}{1:^15}{2:>15}".format(key,present,value))
str2 = ""
for w in words:
    str2 += w[::-1]+" "
print(str2)

print("upper(): "+str.upper())
print("lower(): "+str.lower())
print("isanum(): ",str.isalnum())
print("isalpha(): ",str.isalpha())
print("istitle(): ",str.istitle())
print("replace(a,b): ",str.replace('a','b'))
print("rfind(a): ",str.rfind('a'))
print("endswith(a): ",str.endswith('a'))
print("startswith(a): ",str.startswith('a'))





