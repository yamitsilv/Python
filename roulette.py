budget = 100
endgame = 0
print("Welcome to Roulette!")
print("You start with a budget of ", budget, "tokens")
print("You can exit any time by pressing 'q'")
while budget > 0 and quit == 0:
    import random
    print("To Place a bet please type in a number between 0 and 36")
    value = random.randint(0, 36)
    try:
        bet = input("Place your bet")
        bet = int(bet)
        budget = budget - 1
        if bet == value:
            budget = budget + 36
            print("Correct! You just won 36 tokens! You now have %budget tokens")
        elif 0 <= bet >= 36:
            print("You just wasted a bet on a zero probability to win")
        else:
            print("I'm sorry, it was", value, ". You now have", budget, "tokens")
    except ValueError:
        # Handle the exception
        if bet == 'q':
            endgame = 1
        else:
            print("We're betting on numbers here, but we'll let this one go")
print("Game ended with ", budget, " tokens")