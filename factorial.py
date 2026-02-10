def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)
    
n= int(input("Enter a number :"))

if n < 0:
    print("No factorianl for negative number")
else:
    print(f"Factorial of {n} is {factorial(n)}")