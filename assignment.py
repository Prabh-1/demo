# 1Python program to calculate the length of a string
a='pythonclass'
print ("String is ",(a))
print ("The length of string = ",len(a))

# 2program to count the number of characters (character frequency) in a string. 
x=a.count('p',0,11)
print('p:',x)
x=a.count('y',0,11)
print('y:',x)
x=a.count('t',0,11)
print('t:',x)
x=a.count('h',0,11)
print('h:',x)
x=a.count('o',0,11)
print('o:',x)
x=a.count('n',0,11)
print('n:',x)
x=a.count('c',0,11)
print('c:',x)
x=a.count('l',0,11)
print('l:',x)
x=a.count('a',0,11)
print('a:',x)
x=a.count('s',0,11)
print('s:',x)

c='satisfies'
  
all_freq = {}
  
for i in c:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters in satisfies is :\n "+  str(all_freq))  

# 3Python program to get a string made of the first 2 and the last 2 chars from a given a string
if len(a)<2:
    print ('empty')
print (a[0:2]+a[-2:])

# 4Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
b='satisfies'
char=b[0]
b=b.replace(b[0],'$')
b=char+b[1:]
print(b)
 
# 5program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a='hello'
b='python'
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print (new_a + ' ' + new_b)

# 6Python program to add 'ing' at the end of a given string 
length = len(a)
if length > 2:
  if a[-3:] == 'ing':
    a += 'ly'
  else:
    a += 'ing'
print(a)    

# 7program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
a='this is not okay not poor'
snot = a.find('not')
spoor = a.find('poor')
print(snot)
print(spoor)
if spoor > snot and snot>0 and spoor>0:
   a = a.replace(a[snot:(spoor+4)], 'good')
   print(a)
else:
   print(a)

# 8that takes a list of words and return the longest word and the length of the longest one.
a=['you','are','beautiful']
maxx=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>maxx):
        maxx=len(i)
        temp=i
print ('the longest word is',temp)    
print('length of word is',maxx)    

# 9Python program to remove the nth index character from a nonempty string. 
a='pythonclass'
n=5
frst=a[:n]
scnd=a[n+1:]
print(frst+scnd)

# 10 program to change a given string to a new string where the first and last chars have been exchanged
a='python'
print(a[-1:]+a[1:-1]+a[:1])

# 11program to remove the characters which have odd index values of a given string. 
a='pythonclass'
print(a[::2])

r=''
for i in range(len(a)):
    if i%2==0:
        r=r+a[i]
print(r)

# 12program to count the occurrences of each word in a given sentence. 
line='everything will be best if u try ur best'
word='best'
a=line.split(' ')
print(a)
count=0
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print('count  of word is',count)

# 13Python script that takes input from the user and displays that input back in upper and lower cases
user_input=input('Hello how r u?')
print(user_input.upper())
print(user_input.lower())

# 14program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
sen=input('enter the words:').split(",")
a=list(set(sen))
a.sort()
print(a)

# 15Python function to create the HTML string with tags around the word(s). 
tag='i'
word='python'
print("<%s>%s</%s>"%(tag,word,tag))
print('<',tag,'>',word,'</',tag,'>')

# 16Python function to insert a string in the middle of a string. 
a='python class try'
word='first'
# print(a[:7] + word + a[6:])
for i in range(0,len(a)):
    if(a[i]==' '):
       print(a[:i+1]+word+a[i:])
x=a.split()
print(x)
b=int(len(a)/2)
print(a[:b]+word+a[b:])

# 17Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
a='python'
b=a[-2:]
print(b*4)

# 18Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
a='python'
if(len(a)>3):
   print(a[:3])
else:   
   print(a)

# 19program to get the last part of a string before a specified character


# 20Python function to reverses a string if it's length is a multiple of 4
a='pythonclass'
if(len(a)%4==0):
    print(a[::-1])
else:
    print(a)    

# 21Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters\
a='Prabh'
num=0
for x in a[:4]:
    if(x.upper()==x):
        num+=1
if(num>=2):
    print(a.upper())        
else:
    print(a)    

# 22Python program to remove a newline in Python
a='python class\n'
print(a)
print(a.rstrip())
print(a)

# 23Python program to check whether a string starts with specified characters.
a='Prabh'
print(a.startswith('Pr'))