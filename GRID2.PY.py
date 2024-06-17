import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("3x2 Grid Layout with Different Widgets")

# Define the widgets to be placed in each cell
label = tk.Label(root, text="This is a Label")
button = tk.Button(root, text="Click Me")
entry = tk.Entry(root)
checkbutton = tk.Checkbutton(root, text="Check Me")
radiobutton = tk.Radiobutton(root, text="Option 1")
#listbox = tk.Listbox(root)

# Add some items to the listbox
#for item in ["Item 1", "Item 2", "Item 3"]:
#    listbox.insert(tk.END, item)

# Arrange the widgets in a 4x2 grid
# Full-height column on the left
lbox1.grid(row=0, column=0, rowspan=4, sticky="nsew")
button.grid(row=1, column=1, sticky="nsew")
checkbutton.grid(row=1, column=2, sticky="nsew")
entry.grid(row=2, column=1, sticky="nsew")
radiobutton.grid(row=2, column=2, sticky="nsew")

# Original 2 columns split into 3 rows on the right
label.grid(row=3, column=1, sticky="nsew")

# Configure the grid to make the cells resizable
for i in range(4):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Run the application
root.mainloop()
