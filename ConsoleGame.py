
# python console game
import random

# Function for guessing input
def get_guess():
    n = input("What is your guess")
    l = list(str(n))
    return l

# Generate computer code
def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)
    # Grab first 3
    return digits[:3]


# Clues
def generate_clues(code, user_guess):

    if user_guess == code:
        return "Code Cracked!!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")


    if clues == []:
        return ["Nope"]

    else:
        return clues


# Run Game
print ("Welcome in code breaker !!")

secret_code = generate_code()

print secret_code

print ("Code has been generated, Please guess a 3 digit number by typing")

clue_report = []

while clue_report != "Code Cracked!!":

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)

    print ("Here is the result of your guess: ")

    for clue in clue_report:
        print (clue)
