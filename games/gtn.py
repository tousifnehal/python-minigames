import random
def game():
    number = random.randint(1,100)
    print("✅ Number Generated Successfully")
    
    # Hint For The Generated Number
    
    def hintNumCreator():
        x = random.randint(1,20)
        if x == number :
            return random.randint(1,20)
        if x > number : 
            return random.randint(1,20)
        return x   
    def hintf1():
        p = hintNumCreator()
        return number - p 
    def hintf2():
        q = hintNumCreator()
        return number + q

    hint1 = hintf1()
    hint2 = hintf2()
    
    if number < hint1 or number == hint1 or hint1 < 0:
        if number == 1 or number == 2 or number == 3 or number == 4 or number == 5:
            hint1 = number - 1
        else : 
            hint1 = hintf1()

    if number > hint2 or number == hint2 or hint2 > 100:
        if number == 95 or number == 96 or number == 97 or number == 98 or number == 99:
            hint2 = number - 1
        elif number == 100 :
            hint2 = 100
        else:
            hint2 = hintf2()
            
    # Difficulty Function For Guesses   
    difficulty = int(input("⚡ Difficulty: Choose \n\t1 for Easy (5-10 guesses) \n\t2 for Medium (3-6 guesses) \n\t3 for hard (2-4 Guesses) \n\t4 for extreme hard (1-2) guesses \n"))
    
    
    # if hint1 < number < hint2:
    print(f"💡 Hint: The number is higher than {hint1} and lower or equal than {hint2}.")

    # Easter Egg (5,6,7,8) randomly generated. If Matches It Will Reveal The Number For You :( Don't Try To Cheat 
    egg = random.randint(5,8)
    if difficulty == egg :
        guess = random.randint(1,10)
        print("😲 Oh No! You Knew The Easter Egg. Cheat Mode enabled")
        print("👀 The number Is", str(number))
    elif difficulty == 1 :
        guess = random.randint(5,10)
    elif difficulty == 2:
        guess = random.randint(3,6)
    elif difficulty == 3:
        guess = random.randint(2,4)
    elif difficulty == 4:
        guess = random.randint(1,2)
    else :
        guess = random.randint(1,10)
        print(f"⚠ You Typed {difficulty} that was out of choice, choosing random guesses ")
        
    # Declaring How Many gueeses he have
    print(f"⚡ You Have {guess} guesses")

    # Until The Guess Equals To Zero The Guessing Function will run                   
    while guess != 0 :
        # Asking User What he guessed?
            userg = int(input("❓ Enter Your Guess : ")) 
        # If UserGuess == Number Function
            if userg == number:
                # If User guessed Correctly Congrates Him
                print(f"🎉 Congrats. The Number Was Really {number}.")
                break
            else:
                # For Wrong guesses
                guess = guess - 1
                if userg < number :
                    print(f"You guessed lower, You have {guess} guesses left")
                elif userg > number :
                    print(f"You guessed higher, You have {guess} guesses left")
                # If Guess = 1 It will reveal lucky hint if you have luck
                if guess == 1 :
                    value = random.randint(0,7)
                    h1 = number - value
                    h2 = number + value
                    lucky = random.randint(0,1)
                    if lucky == 0:
                          pass
                    elif lucky == 1:
                        print(f"❗ LUCKY HINT : {h1} < number < {h2}") 
                # If attempts end it will substract 1 score from previous and save
                if guess == 0:  
                
                    print(f"😢 You're out of guesses! The correct number was: {number}.")
                    break
   # If He Wants To Play Again or not function
    def again():
        x = int(input("""\n\nType: \n\t➰ 1 for Playing again\n\t❌ 2 For Exit \n"""))
        return x
  
    choice = again()
    choice
    # if yes than running the whole script again
    if choice == 1 :
        game()
    # If not than checking how many score he have and is it higher than the previous high score
    else:
        print("✅ Thank You For Playing With Me. Exiting Now ")
        exit()
