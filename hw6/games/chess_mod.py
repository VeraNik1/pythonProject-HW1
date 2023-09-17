from random import shuffle as sh


def check_queens(crdnts: list) -> bool:
    """
    Function to check queens position
    :param crdnts: list of queens coordinates
    :return: True if there are no ways for queens to beat each other
    or False if there is at least one way for queens to beat each other
    """
    if (len(set(it[0] for it in crdnts)) != len(crdnts)
            or len(set(it[1] for it in crdnts)) != len(crdnts)):  # checking of rows and coloumns
        return False
    for i in range(len(crdnts) - 1):
        if any([abs(crdnts[i][0] - crdnts[j][0]) == abs(crdnts[i][1] - crdnts[j][1])
                for j in range(i + 1, len(crdnts))]):  # checking of diagonals
            return False
    return True


def show_board(crdnts):
    """
    function to print chess board
    :param crdnts: list of queens coordinates
    :return: print chess board
    """

    print(*list(' abcdefgh'), sep=" ")
    for i in range(1, 9):
        print(9 - i, end='|')
        for j in range(1, 9):
            if (9 - i, j) in crdnts:
                print('Q', end='|')
            else:
                if (i + j) % 2:
                    print("#", end='|')
                else:
                    print(" ", end='|')
        print()
    print('  ', end='')
    print(*range(1, 9), sep='|', end='\n\n')


def hand_queen_placement() -> list:
    """
    function to place queens on the chess board using coordinates from user in format 1, 'h' or 1, 2
     :return: list of queens coordinates
    """
    coordinates = set()
    board_line = 'abcdefgh'
    while len(coordinates) < 8:
        try:
            x, y = input("Input 2 coordinates separated by comma: 1, h or 1, 8\n >>>>  ").replace(" ", "").split(',')
            if int(x) in range(1, 9) and y.isdigit() and int(y) in range(1, 9):
                coordinates.add((int(x), int(y)))
            elif int(x) in range(1, 9) and y in board_line:
                coordinates.add((int(x), board_line.index(y) + 1))
            else:
                print("Incorrect input. Try again")
        except:
            print("Incorrect input. Try again")
    return list(coordinates)


def place_eight_queens_randomly():
    """
    function to place 8 queens on the chess board randomly
    :return: list of queens coordinates
    """
    coordinates = []
    list_i, list_j = list(i for i in range(1, 9)), list(i for i in range(1, 9))
    sh(list_i)
    sh(list_j)
    for i in range(1, 9):
        coordinates.append((list_i[i - 1], list_j[i - 1]))

    return coordinates


def find_list_of_combinations(count=4):
    result = []
    while len(result) < count:
        temp = place_eight_queens_randomly()
        if check_queens(temp):
            if temp not in result:
                result.append(temp)
    return result


"""pairs_1 = [(1, 3), (2, 7), (3, 5), (4, 1), (5, 2), (6, 4), (7, 6), (8, 3)]

pairs = [(2, 'e'), (1, 'g'), (3, 'h'), (7, 'b'), (2, 'a'), (2, 'd'), (8, 'f'), (2, 'c')]

random_board = place_eight_queens_randomly()

show_board(pairs_1)
show_board(pairs)
show_board(random_board)
print(check_queens(pairs_1))
print(check_queens(pairs))

res = find_list_of_combinations()
for item in res:
    show_board(item)

hand_queen_placement()"""
