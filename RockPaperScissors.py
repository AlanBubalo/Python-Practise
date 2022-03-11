while True:
    user1 = input("Player 1, choose between rock, paper or scissors: ")
    user2 = input("Player 2, choose between rock, paper or scissors: ")
    if user1 == user2:
        print("Draw")
    elif (user1 == 'rock') and (user2 == 'scissors'):
        print("Player 1 wins!")
    elif (user1 == 'rock') and (user2 == 'paper'):
        print("Player 2 wins!")
    elif (user1 == 'scissors') and (user2 == 'paper'):
        print("Player 1 wins!")
    elif (user1 == 'scissors') and (user2 == 'rock'):
        print("Player 2 wins!")
    elif (user1 == 'paper') and (user2 == 'rock'):
        print("Player 1 wins!")
    elif (user1 == 'paper') and (user2 == 'scissors'):
        print("Player 2 wins!")
    else:
        print("Wrong inputs")
    more = input("Play more? ")
    if more == "no" or more == "No":
        break;
