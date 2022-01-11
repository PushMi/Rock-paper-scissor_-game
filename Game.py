p1_wins = 0
p2_wins = 0
user1, user2 = None, None


while True:
    if p1_wins == 2 or p2_wins == 2:
        break

    # take inputs from users
    user1 = input("User1 Enter a choice(rock, paper, scissor): ").lower()
    user2 = input("User2 Enter a choice(rock, paper, scissor): ").lower()


    # put conditions 

    if user1 == user2:
        print("both player selected same choice...so it's a tie")
    elif user1 == "rock":
        if user2 == "scissors":
            print("Rock smashes scissors! user1 you win.")
            p1_wins += 1
        else:
            print("Paper covers rock! user2 you win.")
            p2_wins += 1
    elif user1 == "paper":
        if user2 == "rock":
            print("Paper covers rock! user1 you win.")
            p1_wins += 1
        else:
            print("Scissors cuts paper! user2 you win.")
            p2_wins += 1
    elif user1 == "scissors":
        if user2 == "paper":
            print("Scissors cuts paper! user1 you win.")
            p1_wins += 1
        else:
            print("Rock smashes scissors! user2 you win")
            p2_wins += 1

    else:
        print("error")

    print("==========SCORE===========")
    print("Player 1:", p1_wins)
    print("Player 2:", p2_wins)
    print("==========================")

if p1_wins > p2_wins:
    print("Player 1 is the final winner!")
else:
    print("Player 2 is the final winner!")