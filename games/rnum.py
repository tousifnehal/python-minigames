import random
import time

def randomgen():
    urange = int(input("Enter The Range 0 - "))
    num = random.randint(0, urange)
    print("Generating Number...")
    time.sleep(2)
    print(num)