# Operators
# ARITHMETIC OPERATORS
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**2)
print(a%b)

# RELATIONAL OPERATORS
a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(20>15>4<22)

# LOGICAL OPERATORS
a=10
b=20
c=15
print(b>a and b>c)
print(a>b and b>c)
print(b>a or b>c)
print(a>b or b>c)
print(not(b>a and b>c))
print(not(a>b and b>c))
print(not(15>2))

# Bitwise operators
a=4
b=5
print(a&b)
print(a|b)
print(a^b)
print(a>>1)
print(b>>1)
print(a<<1)
print(b<<1)
print(~a)
print(~b)

# Identity operator
a=10
b=10
c=30
print(a is b)
print (a is c)
print(b is not c)

# MEMBERSHIP OPERATOR
a='python'
print('h' in a)
print('k' in a)

# CONTROL FLOW STATEMENTS
# conditional statements
# if statement
x=int(input('enter the number'))
if(x>0):
    print(x,'is positive')

# if-else statement
x=int(input('enter the number'))
if(x%2==0):
    print(x,'is even number')
else:
    print(x,'is odd number')

# nested if else
x=int(input('enter first number'))
y=int(input('enter second number'))
if(x!=y):
    if(x>y):
        print('first number(',x,')is greater than second number(',y,')')
    else:
        print('second number(',y,')is greater than first number(',x,')')
else:
    print('first number(',x,')is equal to second number(',y,')')

# looping statements
# for loop
for x in range(5):
    print(x)

for x in range(5):
    for y in range(5):
        print(x,y)
    print(' ')

for x in range(5):
    for y in range(x+1):
        print('*',end=' ')
    print(' ')

for x in range(5,0,-1):
    for y in range(1,x+1):
        print('*',end=' ')
    print(' ')
    
for x in range(5):
    for y in range(x+1):
        print('*',end=' ')
    print(' ')
for x in range(5,0,-1):
    for y in range(1,x+1):
        print('*',end=' ')
    print(' ')

sum=0
for x in range(1,6):
    sum+=x
print('sum of first 5 natural numbers:',sum)

num='2684'
for i in num:
    print(i,end=" ")

# while loop
num=0
while (num<=10):
    print(num)
    num+=1

num='2473'
sum=0
temp=int(num) 
print('num:',num)
print('digits:')
for i in num:
    print(i)
while temp>0:
    digit=temp % 10
    sum+=digit
    temp//=10
print('sum of digits of num:',sum)

# JUMPING STATEMENTS
# BREAK
for x in range(10):
    print(x)
    if x==5:
        break

for x in range(10):
    if x==5:
        break
    print(x)

for x in range(10):
    if x==5:
        continue
    print(x)

