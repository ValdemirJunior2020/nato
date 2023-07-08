import pandas as pd
import tkinter as tk
from tkinter import font

# Function to handle button click event
def generate_phonetic():
    word = entry.get().upper()
    output_list = [phonetic_dict[letter] for letter in word]
    result_label.config(text=", ".join(output_list).upper(), font=("Arial", 24, "bold"))

# Read CSV file and create dictionary
data = pd.read_csv("nato.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create the GUI windo    
window = tk.Tk()
window.title("NATO Phonetic Alphabet Converter")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 400
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window size and position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create input entry with larger font size
entry_font = font.Font(size=16)
entry = tk.Entry(window, font=entry_font)
entry.pack(pady=20)

# Create button
button = tk.Button(window, text="Convert", command=generate_phonetic)
button.pack()

# Create label for displaying result with larger font size
result_font = font.Font(size=24, weight="bold")
result_label = tk.Label(window, font=result_font)
result_label.pack(pady=20)

# Start the GUI event loop
window.mainloop()
