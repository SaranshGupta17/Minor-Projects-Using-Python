#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!UPGRADED NUMBER GUESSING GAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from ast import Break
import random 
a = int(input("enter your guessing no. \n(Hint): no. is between 0 to 50 :-")) 

winningnumber = random.randint(0,50)
i = 8

while i>0:
    z = i
    z = z-1
    
    if a == winningnumber:
        print(f"Hurrah!! you won in {8-z} attempts. ")
        break
    
    elif z == 0:
        print(f"Game over!! \nWinning no. was {winningnumber}")
        break
    elif a < winningnumber:
        print("Your guess is lower than the winning number. ")
        i = z
        print(f"No. off attempts left {i} ")
        a = int(input("Guess again :- "))
        if a == winningnumber:
            continue

    elif a>winningnumber:
        print("Your guess is greater than the winning number. ")     
        i = z
        print(f"No. off attempts left {i} ")
        a = int(input("Guess again :- "))
        if a == winningnumber:
            continue
    
    else:
        i = z
        print(f"OOPS!! your guess was wrong. \n no. off attempts left {i} ")
        a = int(input("Guess again :- "))
        if a == winningnumber:
            continue
    
            
            


     