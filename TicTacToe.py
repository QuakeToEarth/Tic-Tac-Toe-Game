from tkinter import *
import tkinter.messagebox
bClicked = True
flag = 0


def buttonclicked(b):
    global bClicked, flag
    if bClicked == True and b['text'] == ' ':
        b['text'] = 'X'
        flag = flag+1
        bClicked = False
    elif(bClicked == False and b['text'] == ' '):
        b['text'] = 'O'
        flag = flag+1
        bClicked = True


tk = Tk()
tk.title('TicTacToe')
playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1)

player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1)

label = Label(tk, text='Player 1: ', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text='Player 2: ', font='Times 20 bold',
              bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)


button1 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button3))
button3.grid(row=3, column=2)


button4 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button6))
button6.grid(row=4, column=2)


button7 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='grey', fg='black',
                 height=4, width=12, command=lambda: buttonclicked(button9))
button9.grid(row=5, column=2)

tk.mainloop()
