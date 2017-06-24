__author__="narotham"
# diclaring the list
a = ["anr", 10, 12.2, 'a']
#print(type(a))
#concatinating 2 lists
a= a+[20, "dnasrfkn"]
#print(a)
# appending to a list
a.append(13)
a.append(10)
#print(a)
#print(a[2])
#print(a[6])
#print(len(a))
a.remove(a[2])
#print(a)
a.remove(10)
#print(a)
#print(a)
#print("printing the double increment")
i = 0


#print("printing n")
print(a)
k = 0
for n in range(0, int(len(a)/2)):

    print(a[k])
    k=k+2
    '''
    print(k)
    print(a[k])
    k = k + 2
    '''

'''
console output should look like this:
a
dnasrfkn
10
'''

'''

arr = [3,2,6,4,7]


console output should look like this:
3 + 2
2 + 6
6 + 4
4 + 7

'''
b = [3, 2, 6, 4, 7]
print(b)
print("console output should look like this:")
for n in range(0, 4):
    print(str(b[n]) + " + " + str(b[n + 1]))

# modulus

for n in range(0, len(b)):
    if b[n]%2 == 0:
        print(str(b[n]) + " is even")
    else:
        print(str(b[n]) + " is Odd")

for n in range(0, len(b)):
    if b[n]%2 == 0:
        print("fizz")
    else:
        print("buzz")



'''
console output should look like this:
3 is even
2 is Odd
6 is even
4 is even
7 is even
Odd
'''

'''
if the number is even, print "fizz"
if the number is odd, print "buzz"
'''

for p in range(0,11):
    print(p)
    
 a = [3,2,6,4,7]
for n in range(0, len(a)-1):
    print( str(a[n])+" + "+str(a[n+1]))



