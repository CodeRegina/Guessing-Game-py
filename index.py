def make_guess (guess, answer):
    global score
    make_guessing = True
    attempt = 0
    while make_guessing and attempt < 5:
        if guess.lower() == answer.lower():
           print('Correct Answer')
           score = score + 1
           make_guessing = False
        else:
            if attempt < 2: 
                guess = input('Sorry wrong answer. Please Try Again ')
            attempt = attempt + 1
        

        if attempt == 3:
            print('The correct answer is ' + answer)

    
    score = 0
    print('Guess the food')
    guess1 = input('What shall we eat? ')
    make_guess(guess1, 'Strawberry')
    guess2 = input('Where shall we go ')
    make_guess(guess2, 'park')
    guess3 = input('What game shall we play')
    make_guess(guess3, 'frisbee')


    print('The answer is: ' + str(score))
