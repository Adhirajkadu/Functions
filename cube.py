def cube(num):
    return num*num*num

def by_3(number):
    if number % 3 == 0:
        return cube(number)
    else:
     return False
    
n=int(input("Enter a number to calculate the cube :"))
print(by_3(n))