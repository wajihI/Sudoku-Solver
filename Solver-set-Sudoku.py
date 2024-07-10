board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo): # Going to be called recrusively
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10): # Loop through 1 to 10 and check if it is valid, if true we add it to the board
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo): # Call solve to check if added value is correct
                return True

            bo[row][col] = 0 # If false reset last element (0 in the program means empty space)

    return False


def valid(bo, num, pos): # Need to check row, column and square
    # Checking the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # Searches for the same number we inserted, second part ignores the 'square' we inserted
            return False
    
    # Checking the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Checking the 3x3 box (square)
    # Determines the 'box' top left box is [0,0], top middle is [0,1] top right is [0,2], continue for rest
    box_x = pos[1]  // 3
    box_y = pos[0]  // 3

    for i in range(box_y * 3, box_y * 3 + 3): # If we in box 2, multple by 3 to get index 6 (first element in the top right)
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: # Creates the line for the sudoku, every 3 line based on the first part and 1 != 0 prevents it dispalying the first line
            print("- - - - - - - - - - - - - ") 
    
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
        
            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # rows, columns
    
    return None

# For illustration purposes: 
print_board(board)
solve(board)
print("______________________")
print_board(board)