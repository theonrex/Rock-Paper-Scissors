from random import randint

#moves
moves = ["rock", "paper", "scissors"]

while True:
    computer  = moves[randint(0,2)]
    player = input("r, p or s? (or end game) ").lower()
    if player == "end the game":
        print("Game ended")
        break
    if player == computer :
        print("Tie!")
    elif player == "r":
        if computer  == "p":
            print("You lose", computer , "beats", player)
        else: 
            print("You win!", player, "beats", computer )
            break
    elif player == "p":
        if computer  == "s":
            print("You lose", computer , "beats", player)
        else: 
            print("You win!", player, "beats", computer )
            break
    elif player == "s":
        if computer  == "r":
            print("You lose", computer , "beats", player)
        else: 
            print("You win!", player, "beats", computer )
            break
    else:
        print("wrong input")