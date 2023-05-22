#Tkinter import
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create the main application window
root = tk.Tk()
root.title("Multiple Windows Example")

# Function to open a new window
def open_window():
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Create a grid layout
    new_frame = ttk.Frame(new_window)
    new_frame.grid(column=0, row=0, padx=10, pady=10)

    # Create a scrolling text area
    text_area = tk.Text(new_frame, width=30, height=10)
    text_area.grid(column=0, row=0)
    text_area = scrolledtext.ScrolledText(root, width=40, height=10)
    text_area.pack()

    # Create a custom dialog
    def show_dialog():
        dialog = tk.Toplevel(new_window)
        dialog.title("Custom Dialog")
        ttk.Label(dialog, text="This is a custom dialog!").pack(padx=10, pady=10)

    # Create a button to show the custom dialog
    dialog_button = ttk.Button(new_frame, text="Show Dialog", command=show_dialog)
    dialog_button.grid(column=0, row=1, pady=0)

    # Create a custom widget
    custom_widget = ttk.Label(new_frame, text="Custom Widget")
    custom_widget.grid(column=1, row=0, padx=10)

    # Apply styling with ttk
    style = ttk.Style(new_window)
    style.configure("Custom.TLabel", foreground="blue", font=("Arial", 12))
    custom_widget.configure(style="Custom.TLabel")

# Create a button to open a new window
open_button = ttk.Button(root, text="Open New Window", command=open_window)
open_button.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()


