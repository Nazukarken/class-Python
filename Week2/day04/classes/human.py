from abc import ABC, abstractmethod # The statement from abs import ABC,abstractmethod in Python is used to import necessary tools for creating abstract base classes.

class Human(ABC):
    population=0
    
    #constructor 构造函数
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Human.get_population +=1
        
    #? Behaviors (common methods for all human)
    #eat
    #sleep
    #walk
    #run 
    #communicate
    
    def eat(self):
        print(f"{self.name}is eating.")
        return True
        
    def sleep(self):
        print(f"{self.name}is sleeping")
        return True
        
    def walk(self):
        print(f"{self.name}is walking")
        return True
        
    def run(self):
        print(f"{self.name}is running ")
        return True
        
#communicate method with optional parameters带有可选参数的通信方法
def communicate(self,message="Hello"):
    print(f"{self.name}says,'{message}'")
    return True
    
    
#decorator
@classmethod
def get_population(cls):
    return f"Total number of human:{cls.population}"

@abstractmethod
def work(self):
    pass