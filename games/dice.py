import random
import time

def rolldice():
    dice = random.randint(1,6)
    print("Rolling The Dice....")
    time.sleep(3)
    print(f"You Rolled {dice}")