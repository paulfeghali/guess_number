import random 

''' answer = random.randint(1,10)

while True: 
    guess = input("Guess a number between 1 and 10: ")
    
    if guess.isdigit():
        guess = int(guess)
    else: 
        print("please enter a digit")
        continue
    if guess < answer:
        print("Sorry, guess again. Too low")
    
    if guess > answer: 
        print("Sorry, guess again. Too high")
    
    if guess == answer:  
        print(f"Congrats, you have guessed the number {answer} correctly!")
        break '''
def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else: 
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly! ')

computer_guess(1000)