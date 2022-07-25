from tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1Name = Entry(tk, textvariable=p1, bd=5)
player1Name.grid(row=1, column=1, columnspan=8)
player2Name = Entry(tk, textvariable=p2, bd=5)
player2Name.grid(row=2  column=1, columnspan=8)
