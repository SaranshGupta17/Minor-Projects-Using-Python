#stone paper scissor

# input s p sc
# using while loop
# most no. of times user or computer will win the game 10 chances are given
# no. of time user WON
# no. of times computer WON
import random

def game():
    c = 0
    d = 0
    i = 1
    

    while i<11:
        z = "Stone","Paper","Scissor"
        b = random.choice(z)
        
        print(f"\tROUND{i}")
        a = input("choose any one:-\n> s\n> p\n> sc\nENTER HERE:-")
        
        if a == "s" and b == "Scissor" :
            c += 1
            i += 1
            print("You won!!...But this round ")
            
            continue

        elif a == "p" and b == "Stone":
            c += 1
            i += 1
            print("You won!!...But this round ")
            
            continue
            
        elif a == "sc" and b == "Paper":
            c += 1
            i += 1
            print("You won!!...But this round ")
            
            continue
        else:
            d += 1
            i += 1
            print("You lost!! This round")
            
            continue
        
    print(f"No. of times you won: {c}and No. of times computer won: {d}")
    if c>d:
        print("CONGRATS!!...YOU WON!! ")

    elif c==d:
        print("OOPS!! THATS A TIE.")
        
    else:
        print("SORRY!!..Better luck next time. ")
    
game()