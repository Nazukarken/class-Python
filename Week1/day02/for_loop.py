"""
    FOR LOOP
"""

#with two argument
#print('two argument')
#for i in range(2,10):
 #   print(i)
 
 #with three argument
#print('three argument')
#for i in range(2,16,3):
 #   print(i)
    
#print("backwards")
#for i in range(10,2,-1):
  #  print(i)
    
    
car_list=["Toyota","Honda","Ford","Chevrolet","BMW"]
#for i in range(len(car_list)):
  #  print(car_list[i])
    
#?for each loop
#for i in car_list:
  #  print(i)
    
    
#for i in "string":
   # if i=="i":
    #    print("This is", i)
     #   print(i)




#?while loop
#loop while a certain condition is true
"""
  while condition is true
  do this...
"""
#count=0
#while count<=5:
 #   print("Looping -",count)
  #  count+=2
    
    
    
# - given a list of numbers, return a new list with just the even numbers
#old_list = [3,6,8,9,2,5,6,0,1]
#new_list = []

# your code goes here
#print(new_list)

old_list = [3, 6, 8, 9, 2, 5, 6, 0, 1]
new_list= []

for i in old_list:
    if i % 2 == 0:
        new_list.append(i)
    print(new_list)
