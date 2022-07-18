#1 palindrome program
# user_in=input('enter the string: \n')
# print('the string entered is',user_in)
# if(user_in[::-1]==user_in):
#     print(user_in,'is a palindrome')
# else:
#     print(user_in,'is not a palindrome')    

#2 FACTORIAL PROGRAM    
# def factorial(n):
#     if(n==1 or n==0):
#        return 1
#     else: 
#         return (n * factorial(n-1))
# num=int(input('Enter the number you want to find factorial:'))      
# fact = factorial(num)
# print('factorial of',num,'=',fact)    

#3FIBONACCI SERIES
# def fibonacci(n):
#     if (n==1 or n==0):
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))
# num=int(input('enter number of terms of series:'))
# i=0
# print('Fibonacci Series:')
# while(i<num):
#     print(fibonacci(i))
#     i+=1

#4 Armstrong Number Program
# num=int(input('enter a number:'))
# order=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**order
#     temp//=10
# if num==sum:
#     print(num,"is an Armstrong number")
# else:
#     print(num,"is not an Armstrong number")        

#5 Calculator Program
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print('CALCULATOR')
print('Select Operation:')
print('1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE\n5. EXIT\n')
while True:
    choice=input('Enter choice(1/2/3/4/5):')
    if choice in ('1','2','3','4'):
        num1=float(input('Enter first number:'))
        num2=float(input('Enter second number:'))

        if choice=='1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice=='2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice=='3':
            print(num1,'X',num2,'=',mul(num1,num2))
        elif choice=='4':
            print(num1,'/',num2,'=',div(num1,num2))
    elif choice=='5':
            print('EXIT')
            break
    else:
        print('Invalid choice')

#6 Patterns Program
# for x in range(4):
#     for x in range(4):
#         print('x',end=' ')
#     print(' ')

# for x in range(5):
#     for y in range(x):
#         print('x',end=' ')
#     print(' ')

# for x in range(5):
    # for y in range(x):
    #     print(x,end=' ')
    #     x+=1
    # print(' ')

#7