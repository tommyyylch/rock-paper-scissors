import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Update the result label
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create a canvas
canvas = tk.Canvas(root, width=300, height=200, bg="lightgray")
canvas.pack()

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))

# Place buttons on the canvas
canvas.create_window(100, 150, window=rock_button)
canvas.create_window(150, 150, window=paper_button)
canvas.create_window(200, 150, window=scissors_button)

# Label to display results
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Start the main loop
root.mainloop()
