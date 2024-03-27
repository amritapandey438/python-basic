""" age """
# age=10
# age=18
# age=int(input("enter your name:"))
# age=(type(age))
# print(age)
# if age>=18:
#     print("you can drink")
# else:
#     print("you are under age")  
  

# age=int(input("Enter your age:"))
# if age>=18 and age<50:
#     print("you can drink")
# elif age>50:
#     print("you are too old") 
# else:
#     print("you are under age")       


""" f(format string) used to join str+int"""
# age=int(input("Enter your age:"))
# if age>=18 and age<50:
#     print("you can drink")
# elif age>50:
#     print(f"you are too old because your age is more than {age}") OR (.format(age))
# else:
#     print(f"you are under age because your age is less than {age}")       


# """ Task(HW) """
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=a+b
d=a-b
e=a*b
f=a**b
g=a%b
h=a/b
i=a//b
operators=input("Enter an operator:")
if operators=='+':
    print(f"the sum of a and b is {c}")
elif operators=='-':
    print(f"the difference between a and b is {d}")
elif operators=='*':
    print(f"the multiplication of a and b is {e}")       
elif operators=='**':
    print(f"the square of a with b is {f}")
elif operators=='%':
    print(f"the modulus of a and b is {g}")
elif operators=='/':
    print(f"the division of a by b is {h}")
elif operators=='//':
    print(f"the floordivision of a and b is {i}")
else:
    print("calculation fail")


