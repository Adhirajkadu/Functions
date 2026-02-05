def add(a,b):
    return a+b
def division(a,b):
    return a / b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b

print("Please select the operation. ")
print("a. Add \nb. Substract \nc. Multiply \nd. Division")

choice=input("Please enter your choice(a/b/c/d): ")

n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))

if choice=='a':
    print(n1,'+',n2,'=', add(n1,n2))
elif choice=='b':
    print(n1,'-',n2,'=', substract(n1,n2))
elif choice=='c':
    print(n1,'*',n2,'=', multiply(n1,n2))
elif choice=='d':
    print(n1,'/',n2,'=', division(n1,n2))
else:
    print("Invalid choice")