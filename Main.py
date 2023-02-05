# SNAKE WATER GUN GAME COMPLETED SUCCESSFULLY

# imort random library

import random 
numb= random.randint(1,3)
if numb==1:
    comp="s"
elif numb==2:
    comp="w"
elif numb==3:
    comp="g"

# choose our input for game

you=input("Choose snake(s) | water(w) | gun(g)")

# main game function 

def game(comp,you):
    if comp==you:
        return None

    elif comp=="s":
        if you=="g":
            return True
        if you=="w":
            return False

    elif comp=="w":
        if you=="s":
         return True
        if you=="g":
         return False

    elif comp=="g":
        if you=="w":
         return True
        if you=="s":
         return False

# store function result in a variable and than print choosed turns 

result=game(comp,you)

print("comp choosed = " , comp)
print("You choosed = " , you)

# results declearation of game 

if result==None:
    print("Game is a tie")
elif result:
    print("you win !!!")
else:
    print("You loose")


# congratulations you successfully build your first game 
# khushal sharma !
