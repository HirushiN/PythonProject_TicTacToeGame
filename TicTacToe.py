# initiate the positions of "Tic Tac Toe" game board using a Dictionary.
board_positions = {'1': ' ', '2': ' ', '3': ' ',
                   '4': ' ', '5': ' ', '6': ' ',
                   '7': ' ', '8': ' ', '9': ' '}

# making a list including values of the Dictionary
value_list = []
for position in board_positions:
    value_list.append(position)


# print the initial board
def print_board(board0):
    print(board0['1'] + '|' + board0['2'] + '|' + board0['3'])
    print('-+-+-')
    print(board0['4'] + '|' + board0['5'] + '|' + board0['6'])
    print('-+-+-')
    print(board0['7'] + '|' + board0['8'] + '|' + board0['9'])


# state the main function on the game
def play_game(player_1, player_2):
    player = 'X'
    count = 0
    name = player_1

    # ask to enter a position from the player and store it
    while True:
        print("This is your turn, " + name + ". Move to which place?")
        print_board(board_positions)
        move = input()

        # check the format of the inputs
        if not move.isnumeric():
            print("Invalid input")
        elif int(move) > 9:
            print("Invalid Input")

        # display the symbol in given position
        else:
            if board_positions[move] == ' ':
                board_positions[move] = player
                count += 1
            # if insert position was already filled, display a message
            else:
                print("That place in unavailable.")
                continue

            # state the selection criteria for winners
            if count >= 5:
                if board_positions['1'] == board_positions['2'] == board_positions['3'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['4'] == board_positions['5'] == board_positions['6'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['7'] == board_positions['8'] == board_positions['9'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['1'] == board_positions['4'] == board_positions['7'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['2'] == board_positions['5'] == board_positions['8'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['3'] == board_positions['6'] == board_positions['9'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['1'] == board_positions['5'] == board_positions['9'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

                elif board_positions['3'] == board_positions['5'] == board_positions['7'] != ' ':
                    print_board(board_positions)
                    print("\nGame over.\n")
                    print("***************\n" + name + " won the game\n" + "***************")
                    break

            # when draw the game, display a message
            if count == 9:
                print_board(board_positions)
                print("\nGame over.\n")
                print("It is a Tie!")
                break

            # switch the player according his turn
            if player == 'X':
                player = '0'
                name = player_2
            else:
                player = 'X'
                name = player_1
    # ask for another round from the player
    restart = input("Do u want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        # clear the positions of game board using the list.
        # at next round
        for key in value_list:
            board_positions[key] = " "
        # return to the game.
        play_game(player_1, player_2)


# main function
if __name__ == '__main__':
    print("Enter the name of player 1\n")
    player1 = input()
    print("Enter the name of player 2\n")
    player2 = input()
    print("1 | 2 | 3")
    print("- + - + -")
    print("4 | 5 | 6")
    print("- + - + -")
    print("7 | 8 | 9")
    play_game(player1, player2)
