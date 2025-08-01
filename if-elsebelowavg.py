#write a python program that reads the value of n and check the number zero or non zero
n=int(input("Enter a number: "))
if(n==0):
    print("Entered number is zero")
else:
    print("Entered number is non zero")
     
#write a python program to find largest of two number

a=int(input("enter first number: "))
b=int(input("enter second number: "))
if(a>b):
    print("largest number is: ")
    print(a)
else:
    print("largest number is: ")
    print(b)

#write a program that reads the number and check the numner is positive or not
a=int(input("Enter a number: "))
if(a>0):
    print("Entered number is positive")
else:
    print("entered number is negative")

#write a program to check entered character is vowel or consonant
char=input("Enter a character: ")
if char.lower() in 'aeiou':
    print("character is vowel")
else:
    print("Character is consonant")
    