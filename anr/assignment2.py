'''
arr = [1,3,12,87,65,1,33,22,13,75,76]

final output should be two lists (write code to create two lists which are as follows):
arr1 = [12, 22, 76]
arr2 = [1, 3, 87, 65, 33, 13, 75]
'''

a = [1,3,12,87,65,1,33,22,13,75,76]
b = []
c = []
for n in range(0,len(a)):
    if a[n]%2==0:
        b.append(a[n])
    else:
        c.append(a[n])

print(b)
print(c)
