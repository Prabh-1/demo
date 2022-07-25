#LISTS
l=[2,5,8,4,6,2.4,'hello']
print(l)
print(type(l))
print('elements of list:')
for x in l:
    print(x)
#ADD ELEMENT
a=(input('enter element to be added'))
l.append(a)
print(l)
print('after inserting at 3rd index:')
l.insert(3,7)
print(l)
print('after deleting element from 5th index')
l.pop(5)
print(l)
print('after deleting 5 from list:')
l.remove(5)
print(l)
l1=[1,5,8.3,4,2]
print('after extending list by adding other list')
l.extend(l1)
print(l)
print(l+l1)#other way
print('index of "4"in list')
print(l.index(4))
print('no. of times 4 in list:')
print(l.count(4))
l2=['hello','deep','amaze','full']
print('list:',l2)
print('sorted list:')
l2.sort()
print(l2)
print('list:',l1)
print('sorted list:')
l1.sort()
print(l1)
print('reversed list:')
l1.reverse()
print(l1)

# TUPLE
t=(2,5,3,'hey')
print(t)
print(type(t))
print('elements in tuple:')
for x in t:
    print(x)
print('length of tuple:',len(t))
l=list(t)
print('after converting tuple to list')
print(l)
print('after adding element:')
l.append(5)
print(l)
print('again converting from list to tuple:')
print(tuple(l))

#SETS
s={10,30,50,70}
print(s)
print(type(s))
print('after adding 40:')
s.add(40)
print(s)
print('after removing 50:')
s.remove(50)
print(s)
s1={20,40,60,80}
print('Difference (s-s1):')
print(s.difference(s1))
print('Intersection:',s.intersection(s1))
print(s.isdisjoint(s1))
print(s.issubset(s1))
print(s.issuperset(s1))
s2={10,30,}
print(s2.issubset(s))
print('union:',s.union(s1))

#DICTIONARY
dict1={'k':3,'p':4}
print(dict1)
print(type(dict1))
x=('k1','k2','k3')
y=1
dict1=dict.fromkeys(x,y)
print(dict1)

choice={'fruit':'pear','color':'black','flower':'rose'}
print(choice)
print('choice value of color:',choice.get('color'))
print(choice.get('money',1000))
print('dictionary items:',choice.items())
print('dictionary keys:',choice.keys())
print('dictionary values:',choice.values())
print('setdefault value:',choice.setdefault('fruit','mango'))
choice.pop('fruit')
print('after delete item:',choice)
