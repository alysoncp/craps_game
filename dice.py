# craps game
from time import *


print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~  WELCOME TO CRAPS  ~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

input("Press Enter to continue...")

active = True

money = int(input("How much money are you bringing to the table?"))

# Delay drawing
def roll_graphic():
    print("~")
    sleep(0.5)
    


while (active):
    bet_roll = int(input("Place your bet! ( 2 through 12 )"))
    bet_amount = int(input("How much do you want to wager?"))
    
    input("Press Enter to roll!")
    
    
    
   # if (bet % 2) == 0:
   #     mod = input("Hard %d? [ Y / N ]" % (bet))
        

    import random

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    result = die1 + die2

    #import os
    #os.system('cls')

    def die_print(die):
        if die == 1:
            print("_______")
            print("|     |")
            print("|  o  |")
            print("|_____|")
        if die == 2:
            print("_______")
            print("|o    |")
            print("|     |")
            print("|____o|")
        if die == 3:
            print("_______")
            print("|o    |")
            print("|  o  |")
            print("|____o|")
        if die == 4:    
            print("_______")
            print("|o   o|")
            print("|     |")
            print("|o___o|")
        if die == 5:    
            print("_______")
            print("|o   o|")
            print("|  o  |")
            print("|o___o|")    
        if die == 6:    
            print("_______")
            print("|o o o|")
            print("|     |")
            print("|o_o_o|")     
        
    roll_graphic()
    roll_graphic()
    roll_graphic()
    roll_graphic()
    die_print(die1)
    die_print(die2)
    print("The roll is %d!" % result)

    if result == bet_roll:
        print("YOU WIN!")
        money += bet_amount
    else:
        print("YOU LOOOSE")
        money -= bet_amount
        
    print("You now have %d dollars left" % (money))
    
    j = input("Roll Again? Y/N")
    
    if j == "Y" or j == "y":
        active = True
    else:
        active = False   
        
    
    
    
    