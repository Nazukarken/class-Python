print("Hello world!!")


#?3data type
#String
x ="Hello World Again!"
print(x)
#String
y=45
print(y)

#Boolean
likes_chocolate=True

#?Python Syntax

x=10

if x>50:
    print("Bigger than 50")
else:
    print("Smaller than 50")

if x>25:
    print('x is greater than 5')
else:
    pass

print("Here")

print(type(x))  # check data type

#?String Literal/Concatenation
first_name = "Fred"
last_name = "Flinstone"

#using plus
print(first_name+" "+last_name)

#comma after a strings
full_name=first_name+" "+last_name
print("My name is",full_name)

#Type cast 
total =35
user_val="26"

#total = total + user_val
#print(total)#TypeError

total = total + int(user_val)
print(total)
new_total=str(total) + user_val
print(new_total)

print(f"My name is{first_name}{last_name}")

#?String Built-in functions/methods
lower_case="hello world"
print(lower_case.upper())

upper_case="HELLO WORLD"
print(upper_case.lower())

print(lower_case.count("o"))