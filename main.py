from tkinter import *
from tkinter import ttk

tk = Tk()  # Creates a root window
tk.title("Tic Tac Toe")
frm = ttk.Frame(tk, padding=50)
frm.grid()

frame1 = ttk.Frame(tk, width=100, height=100)
frame1.grid(row=0, column=0)
frame1.grid_propagate(False) #disables resizing of frame
frame1.columnconfigure(0, weight=1) #enables button to fill frame
frame1.rowconfigure(0,weight=1)
box1 = ttk.Button(frame1, text="-")
box1.grid(sticky="wens")

frame2 = ttk.Frame(tk, width=100, height=100)
frame2.grid(row=0, column=1)
frame2.grid_propagate(False) #disables resizing of frame
frame2.columnconfigure(0, weight=1) #enables button to fill frame
frame2.rowconfigure(0,weight=1)
box2 = ttk.Button(frame2, text="")
box2.grid(sticky="wens")

frame3 = ttk.Frame(tk, width=100, height=100)
frame3.grid(row=0, column=2)
frame3.grid_propagate(False) #disables resizing of frame
frame3.columnconfigure(0, weight=1) #enables button to fill frame
frame3.rowconfigure(0,weight=1)
box3 = ttk.Button(frame3, text="")
box3.grid(sticky="wens")

frame4 = ttk.Frame(tk, width=100, height=100)
frame4.grid(row=1, column=0)
frame4.grid_propagate(False) #disables resizing of frame
frame4.columnconfigure(0, weight=1) #enables button to fill frame
frame4.rowconfigure(0,weight=1)
box4 = ttk.Button(frame4, text="-")
box4.grid(sticky="wens")

frame5 = ttk.Frame(tk, width=100, height=100)
frame5.grid(row=1, column=1)
frame5.grid_propagate(False) #disables resizing of frame
frame5.columnconfigure(0, weight=1) #enables button to fill frame
frame5.rowconfigure(0,weight=1)
box5 = ttk.Button(frame5, text="")
box5.grid(sticky="wens")

frame6 = ttk.Frame(tk, width=100, height=100)
frame6.grid(row=1, column=2)
frame6.grid_propagate(False) #disables resizing of frame
frame6.columnconfigure(0, weight=1) #enables button to fill frame
frame6.rowconfigure(0,weight=1)
box6 = ttk.Button(frame6, text="")
box6.grid(sticky="wens")

frame7 = ttk.Frame(tk, width=100, height=100)
frame7.grid(row=2, column=0)
frame7.grid_propagate(False) #disables resizing of frame
frame7.columnconfigure(0, weight=1) #enables button to fill frame
frame7.rowconfigure(0,weight=1)
box7 = ttk.Button(frame7, text="-")
box7.grid(sticky="wens")

frame8 = ttk.Frame(tk, width=100, height=100)
frame8.grid(row=2, column=1)
frame8.grid_propagate(False) #disables resizing of frame
frame8.columnconfigure(0, weight=1) #enables button to fill frame
frame8.rowconfigure(0,weight=1)
box8 = ttk.Button(frame8, text="")
box8.grid(sticky="wens")

frame9 = ttk.Frame(tk, width=100, height=100)
frame9.grid(row=2, column=2)
frame9.grid_propagate(False) #disables resizing of frame
frame9.columnconfigure(0, weight=1) #enables button to fill frame
frame9.rowconfigure(0,weight=1)
box9 = ttk.Button(frame9, text="")
box9.grid(sticky="wens")

tk.mainloop()
