import random  # Import the module named random, to generate random numbers.

guessesTaken = 0  # Create a variable with no value as of yet.

print('Hello! What is your name?')  # Print out the string in the brackets.
myName = input()  # Ask for the users name as an input and assign it to the myName variable.

number = random.randint(1, 20)  # Take a random number between 1 and 20.
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# Take the input from the myName variable and print it out with the strings in the brackets in the given order.

while guessesTaken < 6:  # As long as the value of guessTaken is below 6, repeat the statements in the loop.
    print('Take a guess.')  # Print out the string in the brackets.
    guess = input()  # Ask for an input from the user and assign it to the guess variable.
    guess = int(guess)  # Take the input from the previous line,
# make it an integer and assign it to guess var again.

    guessesTaken += 1  # Add 1 to the value of guessesTaken and assign it to itself.

    if guess < number:  # If the value of guess is bigger then the random value in the number variable,
        print('Your guess is too low.')  # print out the string in the brackets.

    if guess > number:  # If the value of guess is smaller then the random value in the number variable,
        print('Your guess is too high.')  # print

    if guess == number:  # If the value of guess is equal to the random value in the number variable,
        break  # break the loop.

if guess == number:  # If the value of guess is equal to the random value in the number variable,
    guessesTaken = str(guessesTaken)  # Convert the value of guessesTaken and assign it to itself.
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
# Take the strings assigned to the myName and guessesTaken variables and print the out with the strings
# in the brackets in the given order.

if guess != number:  # If the values of guess and number are not equal,
    number = str(number)  # convert the value of number into a string and
    print('Nope. The number I was thinking of was ' + number)  # print it out with the string in the brackets.
