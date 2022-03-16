import random
randNumber = random.randint(1, 45)
# print(randNumber)
guesses = 0
userguess = None
while (userguess != randNumber):
    userguess = int(input("Enter your Guess:"))
    guesses+= 1
    if(userguess == randNumber):
        print("you guessed it right ") 
    else:
        if (userguess>randNumber):
            print("You Guessed It Wrong! Enter a Smaller Number ") 
        else:
            print("You Guessed It Wrong! Enter a Larger Number")

print(f"you guessed the number in {guesses} guesses")
with open("highscore.txt" , "r" ) as f:
    highscore = int(f.read())
if (guesses<highscore):
    print("You Have Just Broken The highscore!")
    with open("highscore.txt",  "w" ) as f:
        f.write(str(guesses))



