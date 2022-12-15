"""
This is a to do list where you can add new items, delete, and
check them.
GD
"""
import tkinter as tk

already_colored = set()


def check():
    """Make the selected item green, but if it's already
    green, make it white again."""

    # Iterating through the selected items
    for item in listbox.curselection():

        # Getting the item name
        item_name = listbox.get(item)

        if item_name in already_colored:
            listbox.itemconfig(item, bg="white")
            # Bacause the item is white, it shouldn't be in the set anymore
            already_colored.discard(item_name)
        else:
            # Make the item green if it isn't in the set
            listbox.itemconfig(item, bg="#b7ec78")
            # Adding the item name into the set
            already_colored.add(item_name)
    
    # Unselecting the items
    listbox.selection_clear(0, "end")


def add_window():
    """Add a new window with an option to add an item or cancel"""

    def add_item():
        """Add item to the listbox"""
        item = entry.get()
        entry.delete(0, "end")
        listbox.insert("end", item)
        # Scrolling to the end of the list so the user can see the new item
        listbox.yview_scroll(listbox.size(), 'units')


    window = tk.Toplevel()
    window.geometry("300x100")

    all_frame = tk.Frame(window)
    all_frame.pack(expand=True)

    entry = tk.Entry(all_frame, font=("", 14))
    entry.pack(pady=15)

    b_frame = tk.Frame(all_frame)
    b_frame.pack()

    add_b = tk.Button(b_frame, text="Add", command=add_item)
    add_b.pack(side="left", padx=10)

    can_b = tk.Button(b_frame, text="Cancel", command=window.destroy)
    can_b.pack()

    entry.focus_set()
    window.bind("<Return>", lambda e: add_item())


def delete_items():
    """Delete selected items"""
    # I'm using reversed so the list doesn't get messed up after
    # the first object is deleted. So it starts deleting from the
    # last to the first object selected
    for item in reversed(listbox.curselection()):
        listbox.delete(item)


root = tk.Tk()
root.geometry("500x500")
root.title("To Do List")

list_frame = tk.Frame(root, bg="blue")
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(
    list_frame,
    width=30,
    height=10,
    font=("times new romans", 20),
    yscrollcommand=scrollbar.set, 
    selectmode="multiple"
)
listbox.pack()

scrollbar.config(command=listbox.yview)

button_frame = tk.Frame(root)
button_frame.pack(pady=40)

delete_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Delete",
    command=delete_items
)
delete_button.grid(row=0, column=0)

add_window_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Add",
    command=add_window
)
add_window_button.grid(row=0, column=1, padx=10)

check_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Check",
    command=check
)
check_button.grid(row=0, column=2)

root.mainloop()
