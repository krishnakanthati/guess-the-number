import random
print("\nWelcome to the Number Guessing Terminal Game!")
print("Coded with ❤ by Kris!")
name = input("\nEnter your First name: ")

print("\n" + name.capitalize() + ", you have 3 chance to guess the correct number.")
number = random.randrange(1, 10)
print("Chances Left: 3")
x = 1
guess = int(input("\nGuess the number between 1 and 10: "))

while (guess != number and x < 3):
    x += 1
    if(x == 2):
        print("Chances Left: 2")
    else:
        print("Chances Left: 1")
    if guess < number:
        print("You need to guess higher. Try again.")
        guess = int(input("\nGuess the number between 1 and 10: "))
    else:
        print("You need to guess lower. Try again.")
        guess = int(input("\nGuess the number between 1 and 10: "))

if guess == number:
    print("You guessed the correct number in " + str(x) + " guess.")
else:
    print("That's incorrect " + name.capitalize() + ". The correct number is " +
          str(number) + ". You are out of chances.")
