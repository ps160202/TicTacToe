from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont

turn = 1
boxes = 0

def checkWinner(box):
    str = ""
    player = ""
    winner = 0

    if turn == 1:
        player = 'O'
        winner = 2
    elif turn == 2:
        player = 'X'
        winner = 1


    if box == 1:
        if((box2['text'] == player and box3['text'] == player) or
                (box4['text'] == player and box7['text'] == player) or
                (box5['text'] == player and box9['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 2:
        if ((box5['text'] == player and box8['text'] == player) or
                (box1['text'] == 'O' and box3['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 3:
        if ((box1['text'] == player and box2['text'] == player) or
                (box5['text'] == player and box7['text'] == player) or
                (box6['text'] == player and box9['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 4:
        if ((box1['text'] == player and box7['text'] == player) or
                (box5['text'] == player and box9['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 5:
        if ((box1['text'] == player and box9['text'] == player) or
                (box3['text'] == player and box7['text'] == player) or
                (box4['text'] == player and box6['text'] == player) or
                (box2['text'] == player and box8['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 6:
        if ((box3['text'] == player and box9['text'] == player) or
                (box4['text'] == player and box5['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 7:
        if ((box1['text'] == player and box4['text'] == player) or
                (box5['text'] == player and box3['text'] == player) or
                (box8['text'] == player and box9['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 8:
        if ((box7['text'] == player and box9['text'] == player) or
                (box2['text'] == player and box5['text'] == player)):
            str = "Player %s wins!" % winner
    elif box == 9:
        if ((box7['text'] == player and box8['text'] == player) or
                (box1['text'] == player and box5['text'] == player) or
                (box3['text'] == player and box6['text'] == player)):
            str = "Player %s wins!" % winner

    if str != "":
        top = Toplevel(tk)
        top.geometry("750x250")
        top.title("Child Window")
        Label(top, text=str).place(x=150, y=80)

    if boxes == 9 and str != "":
        top = Toplevel(tk)
        top.geometry("750x250")
        top.title("Child Window")
        Label(top, text="DRAW!").place(x=150, y=80)














    return


def buttonClick1():
    global turn, boxes
    if(box1['text'] == 'X' or box1['text'] == '0'):
        return
    elif(turn == 1):
        box1['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box1['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(1)
    return


def buttonClick2():
    global turn, boxes
    if(box2['text'] == 'X' or box2['text'] == '0'):
        return
    elif(turn == 1):
        box2['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box2['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(2)
    return


def buttonClick3():
    global turn, boxes
    if(box3['text'] == 'X' or box3['text'] == '0'):
        return
    elif(turn == 1):
        box3['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box3['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(3)
    return


def buttonClick4():
    global turn, boxes
    if(box4['text'] == 'X' or box4['text'] == '0'):
        return
    elif(turn == 1):
        box4['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box4['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(4)
    return


def buttonClick5():
    global turn, boxes
    if(box5['text'] == 'X' or box5['text'] == '0'):
        return
    elif(turn == 1):
        box5['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box5['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(5)
    return


def buttonClick6():
    global turn, boxes
    if(box6['text'] == 'X' or box6['text'] == '0'):
        return
    elif(turn == 1):
        box6['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box6['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(6)
    return


def buttonClick7():
    global turn, boxes
    if(box7['text'] == 'X' or box7['text'] == '0'):
        return
    elif(turn == 1):
        box7['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box7['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(7)
    return


def buttonClick8():
    global turn, boxes
    if(box8['text'] == 'X' or box8['text'] == '0'):
        return
    elif(turn == 1):
        box8['text'] = 'X'
        turn = 2
        boxes
    elif(turn == 2):
        box8['text'] = 'O'
        turn = 1
        boxes

    checkWinner(8)
    return


def buttonClick9():
    global turn, boxes
    if(box9['text'] == 'X' or box9['text'] == '0'):
        return
    elif(turn == 1):
        box9['text'] = 'X'
        turn = 2
        boxes += 1
    elif(turn == 2):
        box9['text'] = 'O'
        turn = 1
        boxes += 1

    checkWinner(9)
    return


tk = Tk()  # Creates a root window
tk.title("Tic Tac Toe")
myFont = tkFont.Font(family='Helvetica', size=20)
frm = ttk.Frame(tk, padding=50)
frm.grid()

frame1 = ttk.Frame(tk, width=100, height=100)
frame1.grid(row=0, column=0)
frame1.grid_propagate(False) #disables resizing of frame
frame1.columnconfigure(0, weight=1) #enables button to fill frame
frame1.rowconfigure(0,weight=1)
box1 = ttk.Button(frame1, text="", command=buttonClick1)
box1.grid(sticky="wens")

frame2 = ttk.Frame(tk, width=100, height=100)
frame2.grid(row=0, column=1)
frame2.grid_propagate(False) #disables resizing of frame
frame2.columnconfigure(0, weight=1) #enables button to fill frame
frame2.rowconfigure(0,weight=1)
box2 = ttk.Button(frame2, text="", command=buttonClick2)
box2.grid(sticky="wens")

frame3 = ttk.Frame(tk, width=100, height=100)
frame3.grid(row=0, column=2)
frame3.grid_propagate(False) #disables resizing of frame
frame3.columnconfigure(0, weight=1) #enables button to fill frame
frame3.rowconfigure(0,weight=1)
box3 = ttk.Button(frame3, text="", command=buttonClick3)
box3.grid(sticky="wens")

frame4 = ttk.Frame(tk, width=100, height=100)
frame4.grid(row=1, column=0)
frame4.grid_propagate(False) #disables resizing of frame
frame4.columnconfigure(0, weight=1) #enables button to fill frame
frame4.rowconfigure(0,weight=1)
box4 = ttk.Button(frame4, text="", command=buttonClick4)
box4.grid(sticky="wens")

frame5 = ttk.Frame(tk, width=100, height=100)
frame5.grid(row=1, column=1)
frame5.grid_propagate(False) #disables resizing of frame
frame5.columnconfigure(0, weight=1) #enables button to fill frame
frame5.rowconfigure(0,weight=1)
box5 = ttk.Button(frame5, text="", command=buttonClick5)
box5.grid(sticky="wens")

frame6 = ttk.Frame(tk, width=100, height=100)
frame6.grid(row=1, column=2)
frame6.grid_propagate(False) #disables resizing of frame
frame6.columnconfigure(0, weight=1) #enables button to fill frame
frame6.rowconfigure(0,weight=1)
box6 = ttk.Button(frame6, text="", command=buttonClick6)
box6.grid(sticky="wens")

frame7 = ttk.Frame(tk, width=100, height=100)
frame7.grid(row=2, column=0)
frame7.grid_propagate(False) #disables resizing of frame
frame7.columnconfigure(0, weight=1) #enables button to fill frame
frame7.rowconfigure(0,weight=1)
box7 = ttk.Button(frame7, text="", command=buttonClick7)
box7.grid(sticky="wens")

frame8 = ttk.Frame(tk, width=100, height=100)
frame8.grid(row=2, column=1)
frame8.grid_propagate(False) #disables resizing of frame
frame8.columnconfigure(0, weight=1) #enables button to fill frame
frame8.rowconfigure(0,weight=1)
box8 = ttk.Button(frame8, text="", command=buttonClick8)
box8.grid(sticky="wens")

frame9 = ttk.Frame(tk, width=100, height=100)
frame9.grid(row=2, column=2)
frame9.grid_propagate(False) #disables resizing of frame
frame9.columnconfigure(0, weight=1) #enables button to fill frame
frame9.rowconfigure(0,weight=1)
box9 = ttk.Button(frame9, text="", command=buttonClick9)
box9.grid(sticky="wens")

tk.mainloop()


