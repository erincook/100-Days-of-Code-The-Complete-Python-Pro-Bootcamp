def check_four(list_to_check):
    # takes a list of values, returns either winner value X or O,or False if no winner
    countX = 0
    countO = 0
    for i in range(len(list_to_check)):
        if list_to_check[i] == "X":
            countX += 1
        elif list_to_check[i] == "O":
            countO += 1

    if countX == 4:
        return "X"
    elif countO == 4:
        return "O"
    else:
        return False


first_empty_slot_dict = {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1}


def check_vertical(board):
    # checks all vertical positions for winners, stopping in each column when it finds a "None" space
    # also fills in the dictionary "first_empty_slot_dict" with the value of the first "None" space in that column
    # returns False if no winner found, and either X or O if a winner is found.

    list_to_check = []
    for column in range(7):
        none_reached = False
        for start_row in range(5, 2, -1):
            if none_reached:
                break
            for row in range(start_row, start_row-4, -1):
                if board[row][column] is None:
                    first_empty_slot_dict[column] = row
                    none_reached = True
                    break
                else:
                    list_to_check.append(board[row][column])
            if not none_reached:
                result = check_four(list_to_check)
                if result == "X" or result == "O":
                    return result
            list_to_check = []
    return False


def check_horizontal(board):
    list_to_check = []
    for row in range(5, -1, -1):
        none_reached = False
        for start_column in range(4):
            for column in range(start_column, start_column+4):
                if first_empty_slot_dict[column] >= row:
                    none_reached = True
                    break
                list_to_check.append(board[row][column])
            if not none_reached:
                result = check_four(list_to_check)
                if result == "X" or result == "O":
                    return result
            list_to_check = []
    return False


def check_left_diag(board):
    list_to_check = []
    result = 0
    for starting_row in range(5, 2, -1):
        row = starting_row
        for starting_column in range(4):
            column = starting_column
            while row > starting_row - 4:
                if board[row][column] is None:
                    break
                else:
                    list_to_check.append(board[row][column])
                row -= 1
                column += 1
            row = starting_row
            if len(list_to_check) == 4:
                result = check_four(list_to_check)
            list_to_check = []
            if result == "X" or result == "O":
                return result
    return False


def check_right_diag(board):
    list_to_check = []
    result = 0
    for starting_row in range(5, 2, -1):
        row = starting_row
        for starting_column in range(6, 2, -1):
            column = starting_column
            while row > starting_row - 4:
                if board[row][column] is None:
                    break
                else:
                    list_to_check.append(board[row][column])
                row -= 1
                column -= 1
            row = starting_row
            if len(list_to_check) == 4:
                result = check_four(list_to_check)
            list_to_check = []
            if result == "X" or result == "O":
                return result
    return False


def check_winner(board):
    vertical_result = check_vertical(board)
    if vertical_result == "X" or vertical_result == "0":
        return vertical_result

    horizontal_result = check_horizontal(board)
    if horizontal_result == "X" or horizontal_result == "O":
        return horizontal_result

    left_diag_result = check_left_diag(board)
    if left_diag_result == "X" or left_diag_result == "O":
        return left_diag_result

    right_diag_result = check_right_diag(board)
    if right_diag_result == "X" or right_diag_result == "O":
        return right_diag_result

    return None



xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O", None),
         (None, "O" , "X" , "X" , "O" , "X", None),
         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins = (("X" , "X" , None, None, None, None, None),
          ("O" , "O" , None, None, None, None, None),
          ("O" , "X" , "O" , "O" , None, "O" , "O" ),
          ("O" , "X" , "X" , "X" , None, "X" , "X" ),
          ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
          ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
print(check_winner(nowins))
