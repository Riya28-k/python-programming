#write a program to print sum of odd numbers upto n
n=int(input("Enter a number: "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=2
    print("sum of odd numbers is:",sum)

#write a program to print sum of even numbers upto n
n=int(input("Enter a number: "))
i=0
sum=0
while i<=n:
    sum+=i
    i+=2
    print("sum of even numbers is:",sum)

#write a program to print natural numbers in reverse order
n=int(input("Enter a number:"))
i=n
while i>=1:
    print(i)
    i-=1

#write a program to print fibnacci series up to n 
n=int(input("Enter a number:"))
a,b=0,1
print("fibonacci series is:")
while a<=n:
    print(a)
    a,b=b,a+b
    n-=1    

#write a program to print factorial of a number
n=int(input("Enter a number:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial of ",n,"is:",fact)
