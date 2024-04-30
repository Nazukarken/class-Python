#Dictionaries/Object
name ="Fred"
hair_color="Brown"
age=34

fred={
    #key    value
    "name":"Fred",
    "hair_color":"Brown",
    "age":34
}

nazuk={
    #key     value
    "name":"Nazuk",
    "hair_color":"Green",
    "age":21
}

print()

#Nested Dictionary
users_list=[{
    
    "name":"Nazuk",
    "hair_color":"Green",
    "age":21
},
           {
    
    "name":"Nazakat",
    "hair_color":"Green",
    "age":21
},
           {
    
    "name":"Maria",
    "hair_color":"Green",
    "age":21
}]

#print(user_list[0]["name"])

#for i in range(len(users_list)):
  #  print(users_list[i]["name"])
   # print(users_list[i]["is_student"])
   
#for each_person_list in users_list:
    #   print(each_person_list["age"])
    
for each_person_list in users_list:
    for key in each_person_list.keys():
        print(each_person_list[key])
        
        
        
user_1 ={  "name":"Nazuk",
    "hair_color":"Green",
    "age":21,"is_student":True,"email":""}

if"email" not in user_1:
    user_1["email"]="nazuk@gmail.com"
else:
    print("Would you like to update email ")
    print (user_1)
    
    
    
#?Function

def simple_function():
    print("Hello World")
    
simple_function()
#Function with parameter
def display_message(message):
    print(message)
    
    display_message("Hello maria")
    
    
    #Function with default parameter and named parameter
    def display_message(message,is_student=True):
        if(is_student):
            print(message.upper())#uppercase
        else:
            print(message)
            
            display_message("hello world")
            display_message("hello world",False)





#return information
def do_calculation(num_1,num_2):
    return num_1 + num_2

result=do_calculation(5,5)
print(result)
print(do_calculation(25,5))


def calculator(operation, x, y):
   
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"

result = calculator('add', 5, 3)
print("Result of addition:", result)

result = calculator('subtract', 10, 4)
print("Result of subtraction:", result)

result = calculator('multiply', 2, 6)
print("Result of multiplication:", result)

result = calculator('divide', 8, 2)
print("Result of division:", result)





items={
    "fruit":{
        "apples":{"quantity":5},
        "bananas":{"quantity":4},
        "watermelon":{"quantity":3}
    }
}