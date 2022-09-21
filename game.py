import random
K = int(input("-------------------------\nhow many times do you want to play\n\n"))
for j in range (K):
    print("-------------------------\nrock - 1\npaper - 2\nscissors - 3\n-------------------------")
    human_turn = int(input())
    computer_turn = random.randint(1,3)

    print()
    if computer_turn == 1:
        print("Computer chose rock\n")
    elif computer_turn == 2:
        print("Computer chose paper\n")
    elif computer_turn == 3:
        print("Computer chose scissors\n")

    if human_turn == computer_turn:
        print("It\'s a tie")
    if human_turn == 1:
        if computer_turn == 2:
            print("Computer wins")
        elif computer_turn == 3:
            print("Human wins")
    elif human_turn == 2:
        if computer_turn == 3:
            print("Computer wins")
        elif computer_turn == 1:
            print("Human wins")
    elif human_turn == 3:
        if computer_turn == 2:
            print("Human wins")
        elif computer_turn == 1:
            print("Computer wins")
print("-------------------------")
