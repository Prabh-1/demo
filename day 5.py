#Functions:
def student():
    print('i am student of ur clg')
student()
def sum(a,b):
    c=a+b
    return c
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
print('sum:',sum(num1,num2))
numbers=[1,4,6,9,2]
print(numbers)
print('sum:',sum(numbers))

# def f1():
    a=10
    b=20
    def f2():
        a=20
        b=30
        return (a+b)
    print('in f2',f2())
    return (a+b)
print('in f1',f1())

# def f1():
    a=20
    def f2():
        global b
        b=10
        print(a)
    f2()
    print(b)
f1()

# defining a function to calculate LCM  
def calculate_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))