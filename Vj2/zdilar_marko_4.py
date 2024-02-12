import random 

wins = [["Rock", "Scissors"], ["Scissors", "Paper"], ["Paper", "Rock"]]


def generateTool():
    computerWeapon = random.randint(0, 2)
    if computerWeapon == 0:
        return "Rock"
    elif computerWeapon == 1:
        return "Scissors"
    else:
        return "Paper"

playerWins = 0
computerWins = 0
maxWins = float(input("Play until: "))


while True:
    playerTool = input("Choose a \"weapon\"(Rock, Scissors, Paper):")
    computerTool = generateTool().lower()
    print("*******************************************************************************")
    print("Player:" + playerTool + "\nComputer:" + computerTool)
    print("*******************************************************************************")

    for win in wins:
        if win[0].lower() == playerTool.lower() and win[1].lower() == computerTool.lower():
            playerWins += 1

        elif win[0].lower() == computerTool and win[1].lower() == playerTool:
            computerWins += 1

    print("Player: " + str(playerWins) + "\nComputer: " + str(computerWins))
    
    if computerWins >= maxWins or playerWins >= maxWins:
        if computerWins > playerWins:
            print("Computer wins by " + str(computerWins) + "-" + str(playerWins))
        else:
            print("Player wins by " + str(playerWins) + "-" + str(computerWins))
        break


        
    


