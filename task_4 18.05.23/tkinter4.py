
#Tkinter import

import os
import tkinter as tk
from tkinter import filedialog, messagebox


Functions(event handling):

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        load_directory(directory)


def load_directory(directory):
    clear_file_list()
    try:
        file_list = os.listdir(directory)
    except OSError:
        messagebox.showerror("Error", "Failed to access directory.")
    else:
        for filename in file_list:
            file_path = os.path.join(directory, filename)
            add_file_to_list(file_path)


def add_file_to_list(file_path):
    file_name = os.path.basename(file_path)
    file_type = "Directory" if os.path.isdir(file_path) else "File"
    file_listbox.insert(tk.END, f"{file_name} [{file_type}]")


def clear_file_list():
    file_listbox.delete(0, tk.END)


def open_selected_file():
    selected_index = file_listbox.curselection()
    if selected_index:
        file_name = file_listbox.get(selected_index[0]).split()[0]
        file_path = os.path.join(current_directory.get(), file_name)
        if os.path.isdir(file_path):
            load_directory(file_path)
        else:
            messagebox.showinfo("Selected File", file_path)


# Create the main window
window = tk.Tk()
window.title("File Explorer")

# Create the file listbox
file_listbox = tk.Listbox(window, width=50)
file_listbox.pack(pady=10)

# Create the scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the file listbox
file_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=file_listbox.yview)

# Create the current directory label
current_directory = tk.StringVar()
current_directory_label = tk.Label(window, textvariable=current_directory)
current_directory_label.pack()

# Create the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

browse_button = tk.Button(button_frame, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=0, padx=5)

open_button = tk.Button(button_frame, text="Open", command=open_selected_file)
open_button.grid(row=0, column=1, padx=5)

# Set the initial directory to the user's home directory
load_directory(os.path.expanduser("~"))

# Start the main loop
window.mainloop()



