

#attribute 属性
class Animal:
     def __init__(self,name,species,age,energy=100):
      self.name = name
      self.species= species
      self.age = age    #all call attribute
      self.energy=energy
      
      
 # Behavior/Methods 行为/方法
      
def sleep(self):
  return f"{self.name}is sleeping!!!"
def walk(self,distance):
    self.energy -= distance #energy =energy - distance
    return f"{self.name} walked{distance}and lost {distance}!.{self.name}has now {self.energy}"

             
def eat(self,food_name,energy):
    self.energy +=energy#energy=energy+energy
    return f"{self.name} ate{food_name} and gained{energy}energy!.now,{self.name}has{self.energy}energy level"
      
      
      
      
  #create a method for animal description that says"{name}is a {species}and is {age}  years old
def get_description(self):


  return f"{self.name}is a {self.species}and is{self.age}years old"
      
      
      
kitty_1 = Animal("Kitty","Cat",4,energy=90)#order of this parameter 该参数的顺序
dog=Animal(species="Dog",name="kitty",age="4",energy=90)#object
      #print(kitty_1)
      
      
      #animals =
      
      #?access to attribute
      #Dictionary-->['key']
print(kitty_1.energy)
      #access to object 访问对象
      
      
      
      
#?access to method 访问方法
print(kitty_1.sleep())
print(dog.sleep())
print(kitty_1.walk(10))


print(kitty_1.eat("Fish",15))
print(dog.eat("Sausage",20))