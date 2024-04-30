table or column unique 
hardly use one to one



users table :
 1.columns

# id (primary key)
First_name--varchar
Last_name--varchar
email--varchar
address--varchar
City--varchar
State--varchar
Password--password

created_at
updated_at


orders table:(1:many user:orders FK=Foreign key )
2.columns
id
state--varchar
created_at
updated_at
pass_order-- boolean
-user_id(it will poop up by it self)


pizzas
create_pizza
3.columns
id
method--varchar
size--int
crust--varchar
quality--varchar 
toppings -- varchar
created_at
updated_at


toppings
-id
-name:varchar(25)
-blah:blah


# only many to many need connection table
pizza_topping
-pizza_id
-topping_id


# queries
Build as you complete each needed table
add 2 users
add 3 pizzas
for Bonus challenge
    add at least 2 toppings to each pizza using a many-to-many relationship
    Skip toppings if you did not add the toppings and pizza_toppings tables
    create an order for one of the users
    2 pizzas







