import random
from classes.food import Food
from classes.player import Player
from classes.weapon import Weapon


player = Player("Fred")

is_playing = True

print(f"Welcome to the game, {player.name}!")
print("Type 'help' for a list of commands.")

# our game loop
while is_playing:

    print(f"\nYour strength is {player.strength}.")
    command = input("Enter a command: ")

    if command == "quit":
        is_playing = False

    elif command == "help":
        print("\nAvailable commands:")
        print("\nquit - quits the game")
        print("help - prints this help message")
        
    elif command =="walk" : 
      #validate     
     """
    choose a direction
    distance/speed
    energy reduction
    feedback - "you walked"
     """
    direction = input("which direction?(e,w,n,s):")
    if direction not in "ewns":
        print("\nYou cannot walk that!")
        continue
    print("\nYou walk"
          +{
              "e":"East",
              "w":"West",
              "n":"North",
              "s":"South"
              
          }[direction])
        
print("Thanks for playing!")
