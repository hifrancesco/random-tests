#primary variables to start the game
secret = "dino"

#the amount of guess each player has to win
failureCount = 6

#this will be used to compare if user entered the correct word
guessedLetters = ""

#iterate through the number of guess
while failureCount > 0:

    #take input from the user [TODO: Validate the input, so user will only input a letter, not words, not emojis, not numbers]
    guess = input ("Enter a letter: ")

    #check if the input is available in the secret phrase
    if guess in secret:
        #user entered a valid letter
        print(f"Correct! There is one or more '{guess}' letters in the secret 🎉")
    else:
        #wrong guess, reduce the guesses remaining
        failureCount -= 1
        print(f"Incorrect! There's no '{guess}' in the secret 😟")

    #
    guessedLetters += guess
    wrongLetterCount = 0

    #visually demonstrate the guessed word
    for letter in secret:
        if letter in guessedLetters:
            print (f"{letter}", end=" ")
        else:
            print ("_", end=" ")
            wrongLetterCount += 1
    print("\n")

    #user guessed all the letters, game complete
    if wrongLetterCount == 0:
        print ("Congratulations! You won the game! 🍾")
        break
else:
    #user ran out of guesses, game over
    print("Sorry, you ran out of guesses 😢! But try again...")