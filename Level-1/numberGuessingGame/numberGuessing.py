import random

low = int(input("please enter lower bound: "))
high = int(input("please enter higher bound: "))

number = random.randint(low, high)

totalNumber = 7
guessCounter = 0

while guessCounter < totalNumber:
    guessCounter += 1
    guess = int(input("Enter Your Guess Number "))

    if guess == number:
     print(f"Correct! Number is {number}. You guessed it in {guessCounter} attempts. ")
     break

    elif guessCounter >= totalNumber and guess != number: 
     print(f"Sorry! number is {number}, Better Luck next time. ")

    elif guess > number:
     print("Too high! Try a lower number.")

    elif guess < number:
     print("Too Low! Try higher one. ")

