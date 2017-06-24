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







