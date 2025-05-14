import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from PIL import Image, ImageTk

# Function to perform the calculation and update the pie chart
def calculate():
    try:
        # Retrieve user inputs
        user_entry_1 = float(entry1.get())
        user_entry_2 = float(entry2.get())
        user_entry_3 = float(entry3.get())
        user_entry_4 = float(entry4.get())
        user_entry_5 = float(entry5.get())
        user_entry_6 = float(entry6.get())

        # Check if user_entry_7 equals the sum of user_entry_1, user_entry_3, and user_entry_5
        user_entry_7 = float(entry7.get())
        if user_entry_7 == (user_entry_1 + user_entry_3 + user_entry_5):
            check_label.config(text="Ok!", fg="green")
        else:
            check_label.config(text="Please double check input", fg="red")

        # Perform the calculation
        result = (user_entry_1 - user_entry_2) + (0.7 * (user_entry_3 - user_entry_4)) + (0.81 * (user_entry_2 + user_entry_4))

        # Display the result in bold font
        result_label.config(text=f"Ile dostane przy wcześniejszym zwrocie?: {result:.2f} zł", font=("TkDefaultFont", 10, "bold"))

        # Update the pie chart with new values
        values = [
            user_entry_1 - user_entry_2,
            user_entry_2,
            user_entry_3 - user_entry_4,
            user_entry_4,
            user_entry_5 - user_entry_6,
            user_entry_6
        ]
        labels = [
            "Suma wpłat\npracownika [zł]",
            "Zysk z wpłat\npracownika [zł]",
            "Suma wpłat\npracodawcy [zł]",
            "Zysk z wpłat\npracodawcy [zł]",
            "Suma wpłat\npaństwa [zł]",
            "Zysk z wpłat\npaństwa [zł]"
        ]
        colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(6)]
        
        ax.clear()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 8})
        canvas.draw()
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Function to clear the entry fields and the graph
def clear():
    for entry in entries:
        entry.delete(0, tk.END)
    ax.clear()
    canvas.draw()
    result_label.config(text="")
    check_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("PPK Kalkulator wcześniejszego zwrotu/wypłaty przed emeryturą")
root.resizable(False, False)  # Lock the window size

# Create and place labels, entry fields, and units
labels = [
    "Suma wpłat pracownika + zysk (1)", "Zysk z wpłat pracownika (2)", "", 
    "Suma wpłat pracodawcy + zysk (3)", "Zysk z wpłat pracodawcy (4)", "", 
    "Suma wpłat państwa + zysk (5)", "Zysk z wpłat państwa (6)", "", 
    "Całkowita kwota na PPK (7)", "", ""
]
units = ["zł", "zł", "", "zł", "zł", "", "zł", "zł", "", "zł", "", ""]

entries = []
for i, label in enumerate(labels):
    if label:
        tk.Label(root, text=label).grid(row=i, column=1, padx=10, pady=5, sticky="e")
    if units[i]:
        entry = tk.Entry(root, width=20)  # Reduce width by 30%
        entry.grid(row=i, column=2, padx=10, pady=5)
        entries.append(entry)
        tk.Label(root, text=units[i]).grid(row=i, column=3, padx=10, pady=5, sticky="w")
    else:
        tk.Label(root, text="").grid(row=i, column=2, padx=10, pady=5)

# Ensure we have exactly 7 entries
entry1, entry2, entry3, entry4, entry5, entry6, entry7 = entries[:7]

# Create and place the additional string below the "Całkowita kwota na PPK" label with smaller font size
additional_string = tk.Label(root, text="Całkowita kwota na PPK = Suma wpłat pracownika+zysk + Suma wpłat pracodawcy+zysk + Suma wpłat państwa+zysk", font=("TkDefaultFont", 8), wraplength=400)
additional_string.grid(row=10, column=1, columnspan=3)

# Create and place the check label below the entry fields with smaller font size
check_label = tk.Label(root, text="", font=("TkDefaultFont", 8))
check_label.grid(row=11, column=1, columnspan=3)

# Create and place the result label two rows below the check label
result_label = tk.Label(root, text="")
result_label.grid(row=13, column=1, columnspan=3)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Oblicz", command=calculate)
calculate_button.grid(row=17, column=1, padx=5, pady=(0, 20))  # Added space below the button

# Create and place the Clear button next to the Calculate button with a small space in between
clear_button = tk.Button(root, text="Wyczyść", command=clear)
clear_button.grid(row=17, column=2, padx=5, pady=(0, 20))  # Added space below the button

# Create a figure for the pie chart
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=0, rowspan=18)

# Load and display the image to the right of the interface
image_path = 'C:\\Users\\WYKURZJ\\Documents\\python files\\2. GUI with tkinter\\gui ppk\\generali2.jpg'
image = Image.open(image_path)
image.thumbnail((832, 737))  # Resize image to fit within specified dimensions
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo_image)
image_label.grid(row=0, column=4, rowspan=18)

# Run the main loop
root.mainloop()