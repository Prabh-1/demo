class student:
    roll_no=10
a=student()
print('roll no:',a.roll_no)

class student:
    def details(self):
        roll_no=20
        name='deep'
        print(roll_no)
        print(name)
a=student()
a.details()

class student:
    def __init__(self):
        print('hii')
a=student()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=student('deep',20)
print(a.name,a.age)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def disp(self,name,age):
        print(name)
        print(self.name)

a=student('prabh',19)
a.disp('deep',20)
print(a.age)

# SINGLE INHERITANCE
class student():
    def details(self):
        name='deep'
        return name

class student2(student):
    def disp(self):
        rn=5
        return rn

a=student2()
print(a.details(),a.disp())

# MULTILEVEL INHERITANCE
class student():
    def details(self):
        name='deep'
        print(name)

class student2(student):
    def disp(self):
        rn=5
        print(rn)

class student3(student2):
    def disp2(self):
        print('done')

a=student3()
a.details() 
a.disp()
a.disp2()

# multiple inheritence
class student():
    def details(self):
        name='deep'
        print(name)

class student2():
    def disp(self):
        rn=5
        print(rn)

class student3(student,student2):
    def disp2(self):
        print('done')

a=student3()
a.details() 
a.disp()
a.disp2()

# heirarchical inheritance
class student():
    def details(self):
        name='deep'
        print(name)

class student2(student):
    def disp(self):
        rn=5
        print(rn)

class student3(student):
    def disp2(self):
        print('done')

b=student3()
a=student2()
a.details() 
a.disp()
b.disp2()
b.details()