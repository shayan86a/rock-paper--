import random
player1 = 0
player2 = 0
while True:
    print(f"Player1: {player1}|| Player2: {player2}")
    list1 = ["rock", "paper", "scissors"]
    a = random.choice(list1)
    b = input("1.rock \n2.paper \n3.scissors \n")
    if b == "end":
        if player1 > player2:
            print("player1 is winner")
        if player1 == player2:
            print("equal")
        if player1 < player2:
            print("player2 is winner")
        break
    print(f"{b} vs {a}")

    if b == "1" or b == "rock":
        if a == "rock":
            print("/\/equal/\/")
        if a == "paper":
            print("/\/lose/\/")
            player2 += 1
        if a == "scissors":
            print("/\/win/\/")
            player1 += 1
    if b == "2" or b == "paper":
        if a == "rock":
            print("/\/win/\/")
            player1 += 1
        if a == "paper":
            print("/\/equal/\/")
        if a == "scissors":
            print("/\/lose/\/")
            player2 += 1
    if b == "3" or b == "scissors":
        if a == "rock":
            print("/\/lose/\/")
            player2 += 1
        if a == "paper":
            print("/\/win/\/")
            player1 += 1
        if a == "scissors":
            print("/\/equal/\/")




