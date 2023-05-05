import random
randNumber = random.randint(1,100)

UserGuess = None
guesses = 0

while(UserGuess != randNumber):

    UserGuess = int(input("Enter your guess: "))
    guesses += 1
    if(UserGuess==randNumber):
        print("you guessed it right")
    else:
        if(UserGuess > randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a larger number")   



print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

if (guesses < hiscore):
    print("you have just broken the hiscore!")    
with open("hiscore.txt" , "w") as f:
    f.write(str(guesses))