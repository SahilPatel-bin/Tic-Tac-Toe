import random
from colorama import Fore
"""
    The code defines a Tic-Tac-Toe game where two players take turns to place their marks on a 3x3
    board, with the game ending when a player wins, or it's a tie.
    
    :param board: The `board` parameter is a 3x3 grid representing the Tic-Tac-Toe board. Each cell in
    the grid can contain either 'O', 'X', or ' ' (empty)
"""
def display_board(board):
    """
    The function `display_board` prints out the contents of a 2D list representing a game board in a
    visually formatted manner.
    
    :param board: The `display_board` function takes a 2D list called `board` as a parameter. This list
    represents the game board, where each element in the list corresponds to a cell on the board. The
    function iterates over the rows and cells in the board and prints out the contents of each
    """
    for row in board:
        for cell in row:
            print(f"{cell} |",end=" ") 
        print()

def is_vaild_move(board,row,col):
    return board[row][col] == ' '

def place_move(board,row,col,player):
    board[row][col] = player

def is_board_full(board):
    for row in board :
        for cell in row:
            if cell == ' ':
                return False
    return True
    
def is_winer(board,player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    #Check cols
    for col in range(len(board[0])):
        if all(board[col][row] == player for row in range(len(board))):
            return True
        
    if all(board[row][row] == player for row in range(0,3)):
        return True
    
    if all(board[row][2-row] == player for row in range(0,3)):
        return True

    return False

def main():  
    board = [[' ' for _ in range(3) ] for _ in range(3)]
    print("Game Start now :-")
    print("--------------------------------------------")
    
    print("Player 1 -> O")
    print("Player 2 -> X")

    player  = 'O'

    while True: 
        player_no = 1 if player == 'O' else 2
        print(Fore.YELLOW + f"\nTurn for player {player_no}\n" + Fore.RESET)
    
        while True :
            if player == 'X':
                row = random.randint(1,3)
                col = random.randint(1,3)
            else :
                row = int(input("Enter the row:- "))
                col = int(input('Enter the column:- '))

            row = row - 1
            col = col - 1

            if is_vaild_move(board,row,col):
                place_move(board,row,col,player)
                break

            else :
                print(Fore.RED + "This place is already use! Enter the other place !\n" + Fore.RESET)
            
        display_board(board)

        if is_winer(board,player):
            print(Fore.GREEN + f"Player {player_no} wins!" + Fore.RESET)
            break

        elif is_board_full(board):
            print(Fore.GREEN + "It is a tie game" + Fore.RESET)
            break

        player = 'O' if player == 'X' else 'X'

main()