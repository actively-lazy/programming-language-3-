from turtle import *
color('blue','red')
begin_fill()
while True:
    forward(200)
    left(170)
    if(abs(pos())<1):
        break
end_fill()
done()
from turtle import *
x=int(input("Enter Radius:"))
pendown()
circle(x)
penup()
area=3.14*x*x
setpos(0,x)
write(area)
done()


color('red')
a = 1
while(a == 1):
    forward(200)
    right(90)
    if(abs(pos())<1):
        break
undo()
done()

pensize(3)
color('blue')
circle(50)
penup()
setposition(100,0)
pendown()
color('red')
circle(50)
penup()
setposition(0,-100)
pendown()
color('green')
circle(50)
penup()
setposition(100,-100)
pendown()
color('black')
circle(50)
penup()
setposition(0,100)
pendown()
done()


pensize(3)
color('green')
circle(50)
penup()
setposition(-120,0)
pendown()
color('yellow')
circle (50)
penup()
setposition(60,60)
pendown()
color('red')
circle (50)
penup()
setposition(-60,60)
pendown()
color('black')
circle (50)
penup()
setposition(-180,60)
pendown()
color('blue')
circle (50)
done()


a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("The addition of 2 nos:",a+b)
print("The subtraction of 2 nos:",a-b)
print("The multipication of 2 nos:",a*b)
print("The division of 2 nos:",a/b)
print("The modulus of 2 nos:",a%b)
print("The integer division of 2 nos:",a//b)
print("The power of 2 nos:",a**b)
