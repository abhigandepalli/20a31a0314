###program to create self arg and acess an obj
class abc:
    attribute =10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.attribute)
obj.display()
##########abhi##########
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is",value)
obj=abc(100)
##########abhi##########
class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the obj value is",var)
        print("the class value is",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)