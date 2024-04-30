from classes.student import Student
from classes.human import Human

#create instance of student class

john = Student ("John",21,"Harvard University")

print(Human.get_population())

print("\nTesting Student Class")
john.eat()
john.sleep()
john.walk()
john.run()
john.study()
john.work()
john.communicate("Hey,I am going to school",words="text")
john.communicate("Hello,where are you?")
