import random


n = int(input("enter a number "))

password =[]

for i in range(0,n):
    f = random.randrange(1, 10)
    password.append(f)

print("your password is", password)