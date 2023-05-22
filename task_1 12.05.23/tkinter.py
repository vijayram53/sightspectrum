#Tkinter import

import tkinter as tk
from tkinter import messagebox, filedialog

# Event handlers
def button_clicked():
    messagebox.showinfo("Button Clicked", "Hello, World!")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write("Sample text saved.")

def show_selection():
    selected_option = dropdown.get()
    messagebox.showinfo("Selected Option", f"You selected {selected_option}")

def draw_shape():
    canvas.create_rectangle(50, 50, 150, 150, fill="blue")
    canvas.create_line(50, 50, 150, 150, fill="red")

# Create main window
window = tk.Tk()
window.title("Basic Window")

# Labels
label = tk.Label(window, text="Hello, World!")
label.pack()

# Buttons
button = tk.Button(window, text="Click Me", command=button_clicked)
button.pack()

save_button = tk.Button(window, text="Save File", command=save_file)
save_button.pack()

# Input widgets
entry = tk.Entry(window)
entry.pack()

dropdown = tk.StringVar()
dropdown.set("Option 1")
dropdown_menu = tk.OptionMenu(window, dropdown, "Option 1", "Option 2", "Option 3")
dropdown_menu.pack()

selection_button = tk.Button(window, text="Show Selection", command=show_selection)
selection_button.pack()

# Dialog boxes
messagebox_button = tk.Button(window, text="Show Message Box", command=lambda: messagebox.showinfo("Message Box", "Hello, Dialog!"))
messagebox_button.pack()

filedialog_button = tk.Button(window, text="Open File", command=lambda: filedialog.askopenfilename())
filedialog_button.pack()

# configure
menubar = tk.Menu(window)
window.config(menu=menubar)

#Menus
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: filedialog.askopenfilename())
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Canvas
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

draw_button = tk.Button(window, text="Draw Shape", command=draw_shape)
draw_button.pack()

# Start the main loop
window.mainloop()
 
