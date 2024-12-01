class Student():
    def __init__(self,name,age,heght,food):
        self.name=name
        self.age=age
        self.food=food
        self.heght=heght
    def show(self):
        print(self.name)
        print(self.age)
        print(self.heght)
        print(self.food)
student1=Student("jake",7,3,"chips")      #making the object for the class
student1.show()
print(student1.age)