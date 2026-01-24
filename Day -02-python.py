#Q34) Number guessing game using python :)
import random
print ("AI Number Guessing Game ")
print ("I am thinking of a number between 1 to 100")
numb = random.randint(1,100)
attem = 0
while True:
  guess = int(input("Enter your Guess:-"))
  attem = attem+1
  if guess < numb:
    print("Too low! Try again.")
  elif guess > numb:
    print("Too high! Try again.")
  else:
    print(f"Correct! The number was {numb}")
    print(f"You Guessed it in {attem} attempts.")
    break
