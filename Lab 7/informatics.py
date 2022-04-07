'''
a=int(input())
b=int(input())
print((a**2+b**2)**0.5)
'''

'''
a = int(input())
b = a-1
c = a+1
print("The next number for the number {0} is {1}.".format(a, c))
print("The previous number for the number {0} is {1}.".format(a, b))
'''

'''
n = int(input())
k = int(input())
print(k//n)
'''


'''
n = int(input())
k = int(input())
print(k%n)
'''

'''
n = int(input())
k = int(input())
print(k*n % 109)
'''
#IF ОПЕРАТОР '''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
n = int(input())
k = int(input())
if n>=k:
    print(n)
else :
    print(k)
    '''
    
'''
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
    '''
    
'''
x = int(input())
y = int(input())
if ((x!=1) & (y!=1)) | ((x==1) & (y==1)):
    print("yes")
else:
    print("No")
    '''
    
    
'''
n = int(input())
##k = int(input())
if n>0:
    print(1)
elif n<0:
    print(-1)
else:
    print(0)
'''


'''
a = int(input())
b = int(input())
if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print(0)
'''
# FOR ЦИКЛ ///////////////////////////////////////////////

'''
a = int(input())
b = int(input())
for i in range(a,b+1):
    if i%2==0:
        print(i)
'''

'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a,b+1):
    if i%c==d:
        print(i)
'''

'''
import math
a = int(input())
b = int(input())
for i in range(a,b+1):
    if  floor(math.sqrt(i))==int(math.sqrt(i)) :
        print(i)
'''


'''
a= int(input())
for i in range(2,a+1):
    if a%i==0:
        print(i)
        break
'''


'''
a= int(input())
for i in range(1,a+1):
    if a%i==0:
        print(i, end = " ")
'''


'''
b = 0
a= int(input())
for i in range(1,a+1):
    if a%i==0:
        b=b+1
        print(b)
'''

'''
c = 0
for i in range(100):
    a =  int(input())
    c = c +a
print(c)
'''

'''
a = int(input())
c = 0
for i in range(a):
    c = c +  int(input())
print(c)
'''


'''
a = int(input())
c = 0
for i in range(a):
    if 0==int(input()):
        c=c+1
print(c)
'''


# WHILE OPERATOR \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    
'''
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
'''

'''
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
'''


'''
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
'''

'''
n = int(input())
k = 2
while k != n:
    if k > n:
        print("NO")
        break
    k = k * 2
else:
    print("YES")
'''


'''
n = int(input())
mass = list(map(int, input().split()))
for i in range(0, n-1):
    elem = mass[i]
    index = i
    if index % 2 == 0:
        print(mass[index], end = ' ')
'''



'''
s=input()
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')
'''

'''
s=input()
a=[int(s) for s in s.split()]
c = 0
for i in a:
    if i>0:
        c =c+1 
print(c)
'''


'''
k = 0
n = int(input())
a = map(int, input().split())
a = list(a)
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        k += 1
print(k)
'''


'''
k = 0
n = int(input())
a = map(int, input().split())
a = list(a)
for i in range(1, len(a)):
    if a[i] > 0 and a[i - 1]>0 or a[i] < 0 and a[i - 1]<0:
        print("yes")
        sys.exit()
'''


'''
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
   
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)
'''


'''
a = input().split()
a = a[::-1]
print(' '.join(a))
'''



# FUNCTIONS//./////...///////////////////////

'''
def min4(a, b, c, d):
    mas = [a,b,c,d]
    mas.sort()
    return mas[0]
 
'''


'''
def powerrr(a,b):
    return(a**b)
'''