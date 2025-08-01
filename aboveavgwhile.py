#write a program to check eneterd number is prime or not 
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")



#write program to find the sum of digit of given number
num = int(input("Enter a number:"))
sum=0
while num >0:
    digit = num % 10
    sum+= digit
    num = num // 10
    print("sum of digit is: ",sum)
    

#write a program to check the enetered number is palindrome or not
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")

#write a program to reverse the given number

num = int(input("Enter a number:  "))
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse * 10 + digit
    num = num // 10
    print("Reversed number is: ",reverse)


    

