#1
def outer_function(a,b):
    def inner_function():
        return a+b
    return inner_function()+5
print(outer_function(1,2))

#2
def largest_of_two(x,y):
    return x if(x>y) else y
def largest_of_three(a,b,c):
    a=largest_of_two(a,b)
    return largest_of_two(a,c)
print('largest of three numbers is : ',largest_of_three(3,1,9))

#3
def sum_of_numbers(*args):
    return sum(args)
def product_of_numbers(*args):
    pro=1
    for i in args:
        pro*=i
    return pro
print('sum of : ',sum_of_numbers(1,2,3,4))
print('product of : ',product_of_numbers(1,2,3,4))

#4
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(0,6):
    print(fib(i))

#5
ch=input('choose 1 for factorial and 2 for fibonacci : ')
match(ch):
    case '1':
        n=int(input("enter the number : "))
        f=1
        for i in range(1,n+1):
            f*=i
        print(f'factorial of {n} is {f}')
    case '2':
        n=int(input('enter the number : '))
        for i in range(0,n):
            if(i==0 or i==1):
                print(i)
            else:
                print((i-1)+(i-2))

#6
n=int(input('enter the number : '))
ch=input('enter 1 to check even or odd 2 to check prime or not : ')
match ch:
    case '1':
        if((n%2)==0):
            print('even')
        else:
            print('odd')
    case '2':
        c=0
        for i in range(2,n):
            if((n%i)==0):
                c+=1
        if c==0:
            print('prime')
        else:
            print('not a prime')

#7
n=input('enter the number or string : ')
if n.isdigit():
    rev=0
    n=int(n)
    t=n
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=int(n/10)
    print(rev)
    if(t==rev):
        print('palindrome')
else:
    rev=''
    for i in range(1,len(n)+1):
        rev+=n[i*-1]
    print(rev)

#8
o=input('enter the order s for straight r reverse : ')
match o:
    case 's':
        for i in range(1,5):
            print(i*'*')
    case 'r':
        for i in range(1,5):
            print((5-i)*'*')

#9
d=dict()
while True:
    k=int(input('enter the roll number : '))
    if(k==0):
        break
    m=int(input('enter the marks : '))
    d[k]=m
print(d)

#10
s=input('enter the string : ')
d=0
u=0
l=0
c=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isupper():
        u+=1
    elif i.islower():
        l+=1
    else:
        c+=1
print(f'uppercase : {u}\nlowercase : {l}\ndigits : {d}\nspecial charectors : {c}')

#11
l=[1,2,3,4]
print(l)
n=int(input('enter the element to be inserted : '))
l.append(n)
print(l)
l.insert(1,9)
print(l)
l.remove(3)
print(l)
l.sort()
print(l)
print(l.index(4))

#12
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print(a.shape)
b=a.reshape(3,4)
print(b)
a=b.reshape(12,)
print(a)
print(b[1])
for i in range(len(a)):
    if(i%2==0):
        print(a[i])

#13
import re

e = input('Enter the mail id: ')
r = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
m = re.match(r, e)
if m:
    print('Valid mail id...')
else:
    print('Invalid mail id...')

e = input('Enter the date: ')
r = r'^[0-9]{2}+-[0-9]{2}+-[0-9]{4}$'
m = re.match(r, e)
if m:
    print('Valid date format...')
else:
    print('Invalid date format...')

#14
import re

e = input('Enter the URL : ')
r = r'^["http://"]["https://"]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
m = re.match(r, e)
if m:
    print('Valid URL...')
else:
    print('Invalid URL...')

e = input('Enter the phone number with country code : ')
r = r'^[+]+[0-9]{2}+[-]+[0-9]{10}$'
m = re.match(r, e)
if m:
    print('Valid phone number...')
else:
    print('Invalid phone number...')