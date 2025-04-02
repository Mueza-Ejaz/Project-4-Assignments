# Project 4: Tic-Tac-Toe Python Project

import tkinter as tk  # GUI (like buttons, windows, labels, etc.)

from tkinter import messagebox # used to show pop-up messages, like displaying the winner of the game.




# Function to check if there is a winner
def check_winner():
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for combo in winning_combinations:
         # Assign individual indices from the current combination to a, b, and c
        a, b, c = combo 

        # Check if all three positions in the current combination have the same text (X or O) and are not empty
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] and buttons[a]["text"] != "":
            # If a player wins, highlight the winning combination in green
            for i in combo:
                buttons[i].config(bg="green")
            
             # Display a message box showing the winning player's symbol (X or O)
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} wins! 🎉")

            root.quit()   # Close the game window (end the game)

              # Return True to indicate that a winner has been found
            return True
        
    # If no winner is found, return False so the game continues    
    return False

# Function that runs when a button is clicked
def button_click(index):
    global current_player, winner  # X/O, True/False

    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # Set the button text to "X" or "O"

        if check_winner():
            winner = True  # Stop the game if there's a winner
        else:
            switch_player()  # Change turns

# Function to switch the current player
def switch_player():
    global current_player # Access the global variable 'current_player'

     # If the current player is "O", switch to "X", otherwise switch to "O"
#      if current_player == "O":
#     current_player = "X"
#   else:
#     current_player = "O"
    
    # shortcut of if-else:
    current_player = "X" if current_player == "O" else "O"

        # Update the label text to show whose turn it is
    label.config(text=f"Player {current_player}'s turn")  


# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the 3x3 grid of buttons:

 # Create an empty list to store the buttons
buttons = []

for i in range(9): 
    btn = tk.Button(root, text="", font=("Arial", 25), width=6, height=2, command=lambda i=i: button_click(i))
    

    btn.grid(row=i // 3, column=i % 3)   # Arrange the button in a 3x3 grid based on its index
     # - row=i // 3 (This divides the index by 3 to determine the row)
     # - column=i % 3 (This uses the remainder when dividing the index by 3 to determine the column)

    buttons.append(btn)  

# Initial settings
current_player = "X"
winner = False

# Label to display whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)  # Place the label below the buttons

# Run the game
root.mainloop()
