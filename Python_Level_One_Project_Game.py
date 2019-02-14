###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you


import random

def generator():
    digits = list(range(10))
    random.shuffle(digits)
    return [str(i) for i in digits[:3]]

num = generator()
print('A three digit code has been generated.')

def game():
    guess = list(input("What's your guess, player? "))
    if guess != num:
        for i in range(len(num)):
            if guess[i] == num[i]:
                print('Match: You\'ve guessed a correct number in the correct position')
                return game()
        if (any (i in guess for i in num)):
            print('Close: You\'ve guessed a correct number but in the wrong position')
            return game()
        else:
            print('Nope: You haven\'t guessed any of the numbers correctly')
            return game()
    else:
        print('You got it right!')

game()
