#write a python program to print the natural number upto n 
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1

#write a python program to print even numbers upto n 
n = int(input("Enter a number: "))
i = 0
while i <= n:
    print(i)
    i += 2

#write a python program to print odd numbers upto n     
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 2

#write a short python program to check wheather the square root of number is prime or not
import math

n = int(input("Enter a number: "))
sqrt_n = int(math.sqrt(n))

if sqrt_n > 1:
    is_prime = True
    for i in range(2, int(sqrt_n ** 0.5) + 1):
        if sqrt_n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(sqrt_n, "is a prime number")
    else:
        print(sqrt_n, "is not a prime number")
else:
    print(sqrt_n, "is not a prime number")



#write a python program to produce following design 
# A B C
# A B C
# A B C
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(3):
         print(chr(65 + j), end=" ")  
    print()



#write a python program to produce following design if user enter 5
# A B C D E
# A B C D
# A B C
# A B
# A
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#write a python program to produce following design if user enter 5
# 1
# 1 2
#  1 2 3 
# 1 2 3 4
# 1 2 3 4 5
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

#write a python program to produce following design is user enter 5
# 1 
# 2 2
# 3 3 3
# 4 4 4 4 
# 5 5 5 5 5
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()

#write a python program to sum of given sequence
#1+1/1!+1/2!+1/...+n!
import math
n = int(input("Enter a number: "))
sum = 0
for i in range(n + 1):
    sum += 1 / math.factorial(i)
print("sum of the series is: ", sum)


       

