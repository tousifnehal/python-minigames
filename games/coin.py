import random
import time

def flip():
    print("Flipping The Coin......")
    time.sleep(3)
    flipval = random.randint(1,2)
    if flipval == 1:
        print("Heads!")
    else:
        print("Tails!")