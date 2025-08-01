#write a python program to print multiplication table
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n, "x", i, "=", n * i)
    i+=1


 #write a program print the n largest numbers
n = int(input("Enter the number of largest elements to find: "))
numbers = []
for i in range (n):
    num = int(input("Enter a number: "))
    numbers.append(num)
    numbers.sort(reverse= True)
    print("The largest", n, "numbers are:", numbers[:n])

##write a program print the n smallest numbers
n = int(input("Enter the number of smallest elements to find: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
    numbers.sort()
    print("The smallest" ,n, "numbers are:" , numbers[:n])
    