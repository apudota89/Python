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

print(".............................................................")

'''
a = [[1,3], [4,9], [5,8], [6,1]]
write code to create a new list as follows:
arr_answer = [4, 13, 13, 7]
'''

a = [[1,3], [4,9], [5,8], [6,1]]
b = []
c = [1,2,[2,3]]
for n in range(0,len(a)):
    c=0
    for m in range(0,len(a[n])):
        c = c+a[n][m]
    b.append(c)
print(b)
