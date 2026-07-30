from random import randint

print("you have 10 guesses")
guess = 10
g = randint(0,80)
movingame = True
while movingame== True:
    num = int(input("guess a number"))
    guess-=1
    print(str(guess)+" guesses remaining")
    if num > g:
        print("guess lower")
    if num < g:
            print("guess higher")
    if guess <= 0:
          print("you are out of guesses you have lost")
          movingame = False 
    if num == g:
            print("correct")
            movingame = False 

