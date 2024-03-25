import random

playerWin = False
player_selection = 0
consoleWin = False

while True:
    console_selection = random.randint(1, 3)
    try:
        player_selection = int(input("\n- Select one:\n·1) Rock\n·2) Paper\n·3) Scissors\n Your choose:\n"))

        if player_selection < 1 or player_selection > 3:
            raise  ValueError("The number shuld be in range of 1 to 3, give another number!")
        else:
            print("Player choosed:" + str(player_selection) + "! and Console choosed: !" + str(console_selection))
            if ((player_selection == 1 and console_selection == 3)
                    or (player_selection == 2 and console_selection == 1)
                    or (player_selection == 3 and console_selection == 2)):
                playerWin = True
            elif player_selection == console_selection:
                print("\nDraw... Choose again!")
                pass
            else:
                consoleWin = True
    except ValueError as e:
        print(e)
        print("Enter only numbers")
    if consoleWin == True:
        print("\nConsole win the game!")
        break
    elif playerWin == True:
        print("\nPlayer win the game!")
        break