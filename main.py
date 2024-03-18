import random
import games.rps as rps
import games.gtn as gtn
import games.dice as dice
import games.coin as fcoin
import games.rnum as randomnum
import games.leapyear as ly
import games.memorychecker as mchk

stars = "*" * random.randint(15,30)

minigames = ["Rock-Paper-Scissors", "Guess The Number", "Roll The Dice", "Flip a coin", "Random Number Generator", "Check Leap Year?", "Memory Checker"]


while True:
    print(stars)
    print("Type The Number Beside The Game To play it \n")
    for i in range(len(minigames)):
        print(f"➡ {i+1} for {minigames[i]}")
    print(stars)
    cmd = int(input("\nWhich One? : "))

    if cmd == 1:
        # pass
        rps.game()    
        
    elif cmd == 2:
        
        gtn.game()
        
    elif cmd == 3:
        
        dice.rolldice()
        
    elif cmd == 4:
        
        fcoin.flip()
        
    elif cmd ==5:
        
        randomnum.randomgen()
        
    elif cmd == 6:
        
        ly.leapyear()
            
    elif cmd == 7:
        
        mchk.memchck()
        
    else:
        print("Unknown Command Choosen")
        break
