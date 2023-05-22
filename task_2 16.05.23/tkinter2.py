#Tkinter import
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog   
#Functions (event handling)
def open_file():
    file_path = filedialog.askopenfilename()
    messagebox.showinfo("Open File", f"Selected file: {file_path}")

def save_file():
      file_path = filedialog.asksaveasfilename()
      messagebox.showinfo("Save File", f"Saved file: {file_path}")

def show_message_box():
    result = messagebox.askquestion("Message Box", "Do you want to proceed?")
    if result == 'yes':
        messagebox.showinfo("Response", "You clicked Yes!")
    else:
        messagebox.showinfo("Response", "You clicked No!")

root = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add file menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a message box menu
message_box_menu = tk.Menu(menu_bar, tearoff=0)
message_box_menu.add_command(label="Show", command=show_message_box)

# Add message box menu to the menu bar
menu_bar.add_cascade(label="Message Box", menu=message_box_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Create a grid layout
frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Add widgets to the grid layout
label = tk.Label(frame, text="Grid Layout Example")
label.grid(row=0, column=0, pady=5)
button = tk.Button(frame, text="Click Me", command=show_message_box)
button.grid(row=1, column=0, pady=5)
# Start the main event loop
root.mainloop()


