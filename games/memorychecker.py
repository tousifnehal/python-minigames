import random
import time
import os

def memchck():
    numlist = []
    usernumlist = []
    numlistrange = random.randint(2,10)
    giventime = random.randint(0,15)

    for i in range(numlistrange):
        number = random.randint(0,100)
        numlist.append(number)
    
    print(f"You Have {giventime}s to remember these")
    print(f"Remember These : {numlist}")
    time.sleep(giventime)

    print("Erasing Numbers")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Total Numbers are {len(numlist)}")
    for i in range(numlistrange):
        getnum = int(input(f"Number {i+1} ? : "))
        usernumlist.append(getnum)
        
    if numlist == usernumlist:
        print("You Have Memorized successfully")
    else:
        print(f"You can't memorized all. \n\tYour Numbers {usernumlist} \n\tThe Given Numbers {numlist}")

