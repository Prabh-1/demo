# a='madam'
# print(a)
# print(a[::-1])
# if(a==a[::-1]):
#     print('it is palindrome')
# else:
#     print ('it is not a palindrome')

# l=[10,20,30]
# for x in l:
#     print(x)

def f1():
    a=10
    def f2():
        print('hello')
        nonlocal a
        a=40
        print(a)
    f2()
f1()