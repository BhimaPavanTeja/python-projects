# import tkinter as tk
#
# root = tk.Tk()
# for i in range(10):
#     w = tk.Label(root, text="Hello, Python")
#     w.pack()
# root.mainloop()

import tkinter as tk

root = tk.Tk()

# List of names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]

for name in names:
    w = tk.Label(root, text=name)
    w.pack()

root.mainloop()
