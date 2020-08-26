# Author: Josh Chen
# Date: 8/26/2020

# Objective: Creating a sudoku solver utilising recursion and backtracking in order to solve the sodoku.
# reason for using this method is that normal greedy methods are too computationally heavy and time consuming.

def solve(board):
    ''' Solve the board one unknown square at a time using recursion and backtracking

        Parameters:
        -----------
        board : 2D array-like
            The current board

        Returns:
        --------
        bool :
            boolean used to determine when the board is fully solved

        Notes:
        ------
        This function is recursive and will utilize backtracking

        Examples:
        ---------
        >>> board = [
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
        >>> solve(board)
        >>> print(board)
        [[7, 8, 5, 4, 3, 9, 1, 2, 6], 
         [6, 1, 2, 8, 7, 5, 3, 4, 9], 
         [4, 9, 3, 6, 2, 1, 5, 7, 8], 
         [8, 5, 7, 9, 4, 3, 2, 6, 1], 
         [2, 6, 1, 7, 5, 8, 9, 3, 4], 
         [9, 3, 4, 1, 6, 2, 7, 8, 5], 
         [5, 7, 8, 3, 9, 4, 6, 1, 2], 
         [1, 2, 6, 5, 8, 7, 4, 9, 3], 
         [3, 4, 9, 2, 1, 6, 8, 5, 7]]
    '''
    # uncomment the following 3 lines to print every step
    # print("                            ")
    # print("****************************")
    # print_board(board)

    #find the next unknown square
    find = find_empty(board)

    #exit the recursive function if there are no unknown squares
    if find == None:
        return True
    else:
        # unpack the tuple containing the x, y of the unknown square
        row, col = find

    # try all the numbers from 1-9
    for i in range(1,10):

        # if one of the numbers from 1-9 is valid set the unknown square to that value 
        if valid(board, i, (row, col)):
            board[row][col] = i

            # Keep going through recursion until a solution is found or backtrack if the solution path is infeasible
            if solve(board):
                return True

            # if the solution path is infeasible backtrack and reset each square back to being unknown (i.e 0)
            board[row][col] = 0

    return False


def valid(board, num, pos):
    ''' Solve the board one unknown square at a time using recursion and backtracking

        Parameters:
        -----------
        board : 2D array-like
            The current board state
        
        num : int
            The intger we wish to try in the unknown square
        
        pos : tuple
            tuple containing the x, y postion of the unknown square

        Returns:
        --------
        bool :
            boolean used to determine whether the num we wish to try is valid in the pos

        Notes:
        ------
        num must be between 1-9
        tuple must be in the format x(row), y(column)
    '''
    # Check if num is valid within its row 
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if num is valid within its column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # floor division to find where the start of the box is
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    # Check if num is valid within its 3x3 box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board):
    ''' Solve the board one unknown square at a time using recursion and backtracking

        Parameters:
        -----------
        board : 2D array-like
            The current board state 

        Returns:
        --------

        Notes:
        ------
        This function outputs a visualized board for the user to easily read
    '''
    for i in range(len(board)):
        if i % 3 == 0:
            print(" --------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    ''' Solve the board one unknown square at a time using recursion and backtracking

        Parameters:
        -----------
        board : 2D array-like
            The current board state 

        Returns:
        --------
        (i, j) : int tuple
            The next unknown square
            
        None :
            returns None if there isnt a unknown square left on the board

        Notes:
        ------
        This function contains the exit condition for the recursive function which is when there are no unknown squares
        left on the board
    '''
    # Loop through the entire grid looking for the next unknown square 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # return the unknown square as a tuple
                return (i, j)  # row, col

    return None

if __name__ == "__main__":
    #Enter the unsolved sodoku board that the user wishes to solve into this 2D array.
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

    #displaying the board the user enter
    print_board(board)
    solve(board)
    print("                            ")
    print("****************************")
    #displaying the solved board
    print_board(board)
    pass
