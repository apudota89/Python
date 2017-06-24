__author__="narotham"
'''

write a class student: the class attributes are: name, age, gender, school
initialize 3 students - any name, age, gender, and initialize school for each with default value


'''

# defining the class stdent with name, age, gender and school with default

class student():
    def __init__(self,name,age,gender,school="SSM"):
        self.name=name
        self.age=age
        self.gender=gender
        self.school=school
    def print_student(self):
        print("-------------------------------")
        print("student name: "+self.name)
        print("student age: "+str(self.age))
        print("student gender: "+self.gender)
        print("student school: "+self.school)
        print("")
        print("")
a = student("Narotham",28,"M")
b = student("Rohan",25,"M")
c = student("Raj",26,"F")
a.print_student()
b.print_student()
c.print_student()


print("......................................................")
'''class phone():
    def __init__(self):
        print("hello")
    def method1(self,model):
        print(type(model))
      #  print("model of phone as" + model)
a = phone()
a.method1(10)
'''



class phone():
    processor = "amd"
    color = "Red"
    size = 7.2


    def __init__(self,processor,color,screen_size):
         self.processor=processor
         self.color=color
         self.screen_size=screen_size

    def print_pro(self):
        print("processor is "+self.processor)
        print("color is "+self.color)
        print("screen size is "+str(self.screen_size))

a=phone("Intel","Black",11.2)
a.print_pro()









 
