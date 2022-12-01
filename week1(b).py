#if else condition,else comes after if conditiion
#example
age=int(input())
if age>14:
    print("your are above 14")
else:
    print("you are below 14 ")

#pass statement skips the whole condition and prints nothing
if age<14:
    pass
#nested if else
a=24
b=int(input())
if a==b:
    print('you win')
else:
    if a<b:
        print('too low')
    else:
        print('too high')

#if elif else statement used for multiple conditions
#example
# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)
Age=int(input())
if 0<Age<=3:
    print('ticket price : Free')
elif 3<Age<=10:
    print('ticket price : 150 ')
elif 10<Age<=60:
    print('ticket price : 250 ')
else:
    print('ticket price : 200 ')


#check empty or not
# example
nam=input()
if nam:             #true if string input
    print('str is not empty')
else:
    print('string is empty')
