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










