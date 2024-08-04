from tkinter import *
import random

# Define the magic square
magic_square = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

# Initialize the game state
states = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Function to check for a winner
def check_winner():
    for row in states:
        if row[0] == row[1] == row[2] != 0:
            return row[0]
    for col in range(3):
        if states[0][col] == states[1][col] == states[2][col] != 0:
            return states[0][col]
    if states[0][0] == states[1][1] == states[2][2] != 0:
        return states[0][0]
    if states[0][2] == states[1][1] == states[2][0] != 0:
        return states[0][2]
    return None

# Function to get indices from magic square value
def get_indices(value):
    for i in range(3):
        for j in range(3):
            if magic_square[i][j] == value:
                return (i, j)
    return None

# Function to make AI move based on magic square logic
def ai_move():
    player_indices = [(i, j) for i in range(3) for j in range(3) if states[i][j] == 'X']
    ai_indices = [(i, j) for i in range(3) for j in range(3) if states[i][j] == 'O']

    # Check if AI can win
    for i in range(len(ai_indices)):
        for j in range(i + 1, len(ai_indices)):
            sum_val = magic_square[ai_indices[i][0]][ai_indices[i][1]] + magic_square[ai_indices[j][0]][ai_indices[j][1]]
            if sum_val < 15:
                target = 15 - sum_val
                move = get_indices(target)
                if move and states[move[0]][move[1]] == 0:
                    states[move[0]][move[1]] = 'O'
                    b[move[0]][move[1]].configure(text='O')
                    return

    # Block player's winning move
    for i in range(len(player_indices)):
        for j in range(i + 1, len(player_indices)):
            sum_val = magic_square[player_indices[i][0]][player_indices[i][1]] + magic_square[player_indices[j][0]][player_indices[j][1]]
            if sum_val < 15:
                target = 15 - sum_val
                move = get_indices(target)
                if move and states[move[0]][move[1]] == 0:
                    states[move[0]][move[1]] = 'O'
                    b[move[0]][move[1]].configure(text='O')
                    return

    # If no winning or blocking move, choose a random empty cell
    empty_cells = [(i, j) for i in range(3) for j in range(3) if states[i][j] == 0]
    if empty_cells:
        move = random.choice(empty_cells)
        states[move[0]][move[1]] = 'O'
        b[move[0]][move[1]].configure(text='O')

# Callback function for button click
def callback(r, c):
    if states[r][c] == 0:
        b[r][c].configure(text='X')
        states[r][c] = 'X'
        winner = check_winner()
        if winner:
            print(f"Winner is {winner}")
        else:
            ai_move()
            winner = check_winner()
            if winner:
                print(f"Winner is {winner}")

# Initialize the Tkinter window
root = Tk()
b = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=4, bg='green', command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

root.mainloop()
