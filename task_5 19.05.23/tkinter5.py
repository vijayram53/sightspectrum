#Tkinter imports

import tkinter as tk
from tkinter import ttk


def on_drag_start(event):
    # Get the index of the selected item
    selected_index = listbox1.curselection()[0]
    # Get the text of the selected item
    selected_text = listbox1.get(selected_index)
    # Set the drag data (the selected text) to be dragged
    event.widget.selection_own()
    event.widget.setvar('selected_text', selected_text)


def on_drag_enter(event):
    event.widget.selection_own()


def on_drop(event):
    # Get the drag data (selected text)
    selected_text = event.widget.getvar('selected_text')
    # Insert the dragged item into the target listbox
    event.widget.insert(tk.END, selected_text)
    # Delete the item from the source listbox
    listbox1.delete(listbox1.curselection())
    event.widget.selection_clear()


root = tk.Tk()

# Create the listbox widgets
listbox1 = tk.Listbox(root)
listbox2 = tk.Listbox(root)

# Insert some initial items in the first listbox
for i in range(1, 6):
    listbox1.insert(tk.END, f"Item {i}")

# Bind the drag start event to the first listbox
listbox1.bind("<<ListboxSelect>>", on_drag_start)
listbox1.bind("<B1-Motion>", on_drag_start)

# Bind the drag enter and drop events to the second listbox
listbox2.bind("<B1-Motion>", on_drag_enter)
listbox2.bind("<ButtonRelease-1>", on_drop)

# Place the listboxes in the window
listbox1.grid(row=0, column=0, padx=10, pady=10)
listbox2.grid(row=0, column=1, padx=10, pady=10)

#Window loop

root.mainloop()

