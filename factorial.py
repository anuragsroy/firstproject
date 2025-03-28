def fact(num):
    num2 = 1
    for i in range(num, 0, -1):
        num2 = num2 * i
    return num2
n=int(input("Enter the number"))
print("Factorial of",n,"is: ",fact(n))