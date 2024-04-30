from classes.human import Human


class Student(Human):
    #refer
    #constructor
    def __init__(self, name, age,school):
        super().__init__(name, age,)
        self.school =school
        
     #Implementation of abstract method 抽象方法的实现
    def work(self):
         print(f"{self.name},the student,is studying at{self.school}")
            
    #Polymorphism 多态性-- overloading and overriding 重载和覆盖
    def communicate(self,message="Hello",words="text"):
      if words == "text":
        print(f"{self.name},the student,texts:'{message}'")
      else:
        print(f"{self.name},the student,says loudly:'{message}'")
        
        
    #Additional method to student 学生的附加方法
    def study(self):
        print(f"{self.name}is studying")