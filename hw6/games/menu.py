
from chess_mod import show_board, check_queens, hand_queen_placement, place_eight_queens_randomly, \
    find_list_of_combinations


def menu_chess():
    while True:
        print("Choose one of the options below: \n"
              "1 - to input coordinates for 8 queens and check if they can't beat each other\n"
              "2 - to get random board with 8 queens and check if they can't beat each other\n"
              "3 - to get 4 random boards with 8 queens which can't beat each other\n"
              "q - for exit\n")

        choice = input().lower()

        match choice:
            case "1":
                coordinates = hand_queen_placement()
                show_board(coordinates)
                print(f"Queens can {'not' * check_queens(coordinates)} beat each other\n")

            case "2":
                coordinates = place_eight_queens_randomly()
                show_board(coordinates)
                print(f"Queens can {'not' * check_queens(coordinates)} beat each other\n")
            case "3":
                result = find_list_of_combinations()
                for board in result:
                    show_board(board)
                    print(f"Queens can {'not' * check_queens(board)} beat each other\n")
            case "q":
                exit()
            case _:
                print("Wrong input\n")


menu_chess()