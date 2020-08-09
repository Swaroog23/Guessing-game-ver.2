def guess_num():
    """Simple game where you imagine a number and  the computer has to guess the number with some command lines"""

    print('Imagine a number between 1 and 1000 and i will guess it in 10 tries! '  
          'Use this lines to guide me: "Too big", "Too small", "You win"')

    minimum = 0
    maximum = 1000
    correct = False
    turns = 0

    while not correct:

        guess = int((maximum - minimum) / 2) + minimum

        print(f"My guess is: {guess}")

        answer = input().lower()

        if answer == "you win":
            correct = True 
        elif answer == "too big":
            turns += 1
            maximum = guess
        elif answer == "too small":
            turns += 1
            minimum = guess
        else:
            print('Use this lines to guide me: "Too big", "Too small", "You win"')

    return f"I guessed in {turns} moves!"
