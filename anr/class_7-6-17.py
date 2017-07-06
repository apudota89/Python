'''
arr = [4,2,7,4,3]
print the sum of the numbers in the array

a = [4,2,7,4,3]
j=0
for n in range(0,len(a)):
     j=j+a[n]

print(j)
'''

'''
arr = [4,1,6,3]
arr2 = [1,5,2,3]

                answer should be: arr3 = [5, 6, 8, 6]
                (hint: arr[0] + arr2[0], arr[1] + arr2[1], …)
a=[4,1,6,3]
b=[1,5,2,3]
c=[]

for n in range(0,len(a)):
    c.append(a[n]+b[n])
    #c[n]=a[n]+b[n]

print(c)

'''

'''
Create a class named Fruit.  The class attributes are: name = string, berry = true or false (boolean)
Create 4 instances of Fruit with name and if it is a berry or not: apple, mango, watermelon, strawberry
Put all the berries in one array, and all the non-berries in one array.  Example: berries = [“strawberry”] , non-berries  = [“apple”, “mango”, “watermelon”]
class fruit():

    def __init__(self,name,berry = True|False):
        self.name = name
        self.berry = berry


a = fruit("apple",False)
b = fruit("mango", False)
c = fruit("watermelon",False)
d = fruit("strawberry",True)

berries=[]
non_berries=[]
if a.berry == True:
    berries.append(a.name)
else:
    non_berries.append(a.name)
if b.berry == True:
    berries.append(b.name)
else:
    non_berries.append(b.name)
if c.berry == True:
    berries.append(c.name)
else:
    non_berries.append(c.name)
if d.berry == True:
    berries.append(d.name)
else:
    non_berries.append(d.name)

print(berries)
print(non_berries)
'''
berries=[]
non_berries=[]
class fruit():

    def __init__(self,name,berry=True|False):
        self.name = name
        self.berry = berry
    def decision(self):
        if self.berry == True:
            berries.append(self.name)
        else:
            non_berries.append(self.name)





a = fruit("apple",False)
b = fruit("mango", False)
c = fruit("watermelon",False)
d = fruit("strawberry",True)
a.decision()
b.decision()
c.decision()
d.decision()

print(berries)
print(non_berries)












