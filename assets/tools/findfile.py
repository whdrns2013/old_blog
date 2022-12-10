import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.geometry('320x240')
root.title('abc')

frame = tk.Frame(root)
frame.pack()

path1 = fd.askopenfilename(initialdir='/',title="select a file",
                          filetypes =(("Python files","*.py"),
                                      ("txt files","*.txt"),("all files","*.*")))