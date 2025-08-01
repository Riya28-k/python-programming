#write program to eveluate the student performance
percentage=float(input("Enter percentage:"))
if(percentage >= 90):
    print("Excellent performance")

elif percentage>=80:
    print("Very good performance")

elif percentage>=70:
    print("Good performance")

elif percentage>=60:
    print("Avarage performance")

else:
    print("poor performance")

#write a python program to find largest of tree numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a>b and a>c):
    print("largest number is: ")
    print(a)
elif(b>c and b>a):
    print("largest number is: ")
    print(b)
else:
    print("largest number is:")
    print(c)

#write a python program to find smallest of tree numbers       
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a<b and a<c):
    print("smallest number is: ")
    print(a)
elif(b<c and b<a):
    print("smallest number is: ")
    print(b)
else:
    print("smallest number is:")
    print(c)