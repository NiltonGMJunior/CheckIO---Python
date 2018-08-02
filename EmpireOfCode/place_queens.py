def setBoard(board, piece_file, piece_row):
    '''Attempts to place a piece on the board. Returns the updated board if possible (i. e. queens are not attacking each other), and -1 if there is interference.'''
    new_board = board
    # Procedure for placing all the interferences on the row of the queen
    for i in range(8):
        if i == piece_file:
            continue
        if board[piece_row][i] == 0:
            new_board[piece_row][i] = 'X'
        else:
            return -1
    
    # Procedure for placing all the interferences on the file of the queen
    for i in range(8):
        if i == piece_row:
            continue
        if board[i][piece_file] == 0:
            new_board[i][piece_file] = 'X'
        else:
            return -1

    # Procedure for placing all the interferences on teh diagonals of the queen
        # Going upwards and to the left:
    while True:
        current_row = piece_row
        current_file = piece_file
        if current_row + 1
        


    return new_board

def place_queens(pieces):

    board = [[0]*8]*8 # Sets the board as all 0s (empty spaces)
    positions = []
    # The following for loop places the first pieces on the board and checks if the initial arrangement is legal
    for piece in pieces:
        piece_row = piece[1] - 1 # Rows 1-8 maped to indexes 0-7
        piece_file = ord(piece[0].lower()) - ord('a') # Files a-h maped to indexes 0-7
        if board[piece_row][piece_file] == 0:
            board[piece_row][piece_file] = 'Q' # Sets the queen if tile is empty (no queen) and is not attacked
            board = setBoard(board, piece_file, piece_row) # Places interferences on board
            if board == -1: # The board is illegal
                return () # Returns empty set
            else: # Board is legal
                positions.append(piece)

    piecesLeft = 8 - len(positions) # Number of queens that are yet to be placed on the board        

    return 

def main():
    pieces = #Insert a test set here!!!
    place_queens(pieces)
    return

if __name__ == "__main__":
    main()