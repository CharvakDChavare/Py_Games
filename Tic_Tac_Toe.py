def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]  # diags
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

def is_tie(board):
    return "-" not in board

def tic_tac_toe():
    board = ["-"] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions: 1|2|3")
    print("         4|5|6")
    print("         7|8|9")
    print()
    
    while True:
        print_board(board)
        
        try:
            pos = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
            if 0 <= pos <= 8 and board[pos] == "-":
                board[pos] = current_player
                
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                if is_tie(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid position! Choose an empty spot 1-9.")
        except ValueError:
            print("Enter a valid number 1-9!")

if __name__ == "__main__":
    tic_tac_toe()
