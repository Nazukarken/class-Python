#?else statement
if 1 == 2:
    print("true")
else:
    print("not true")


likes_chocolate = 0

if likes_chocolate is not True:
    print("I like chocolate")
else:
    print("I don't like chocolate")
    
    
    
    age= 11
    name="Fred"
    if age<=12:
        print(f"{name}is a child")
    elif age<=19:
        print(f"{name}is a teenager")
        
        
        
#?Modules
#it does the division and returns the remainder
line_number = 6
#print(line_number%3)
if(line_number%2==0):
    print("Highlight the line")
else:
    print("Don't highlight the line")


#Write a Python program that classifies a given number into different categories.
# To classify the number into one of the following categories:
# If the number is even, print "The number [number] is even."
# If the number is odd, print "The number [number] is odd."
# If the number is zero, print "The number is zero."
# If the number is negative, print "The number [number] is negative."
        
 
categories_number= 9

if (categories_number%2 == 0):
    print(f"The number {categories_number}is a even")
elif (categories_number == 0):
    print(f"The number is zero ")
elif (categories_number<0 ):
    print(f"The number{categories_number} is a negative")
if(categories_number%2 ==1):
    print(f"The number{categories_number} is a odd")
