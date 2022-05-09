from threading import main_thread
import tkinter as tk
from tkinter import ttk,PhotoImage
from typing import Counter
from PIL import Image,ImageTk
win = tk.Tk()
win.geometry("500x600+430+25")

win.resizable(False, False)

load = Image.open(r"BASE.jpg")
bg_image = ImageTk.PhotoImage(load)
base= ttk.Label(win,image=bg_image)
base.place(x=-2,y=-2)

mainframe = tk.Frame(win,bg = "white")
mainframe.place(x = 67,y = 117)

def validate(P):
    if len(P) == 0:
        return True
    elif len(P) == 1 and P.isdigit():
        return True
    else:
        return False

vcmd = (win.register(validate), '%P')

d= {}
for i in range(81):
    a = str(i)
    d[a] = tk.StringVar()
counter = 0
rcounter =0
xa = 73
ya = 120
for i in d:
    tr = 's'+i
    tr = tk.Entry(win,bd=0,font=("Burbank Big Cd Bk",25),validate="key", validatecommand=vcmd,textvariable=d[i])

    tr.place(x = xa,y=ya,height=30,width = 28)
    counter+=1
    rcounter+=1
    if counter ==3:
        xa+=50
        counter = 0
    else:
        xa += 38
    if rcounter%9==0:
        xa = 73
        if rcounter%27 ==0:
            ya+=50
        else:
            ya+=38
        

l = []
puzzle = []
def sub():
    for i in d:
        a = d[i].get()
        if a=='':
            l.append(-1)
        else:
            l.append(int(a))
    for i in range(9,82,9):
        puzzle.append(l[(i-9):i])

def find_empty_space(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==-1:
                return i,j
    return None,None
        
def valid(puzzle,guess,r,c):
    rv = puzzle[r]
    if guess in rv:
        return False
    cv = [puzzle[i][c] for i in range(9)]
    if guess in cv:
        return False
    
    row_start = (r//3)*3
    col_start = (c//3)*3
    for i in range(row_start,row_start+3): 
        for j in range(col_start,col_start+3):
            if puzzle[i][j] == guess:
                return False

    return True


def solver(puzzle):
    r,c = find_empty_space(puzzle)
    if r is None:
        return True
    for guess in range(1,10):
        if valid(puzzle,guess,r,c):
            puzzle[r][c] = guess
            if solver(puzzle):
                return True 
        puzzle[r][c]= -1

    return False 

def solve():
    al = []
    sub()
    a = solver(puzzle)
    if a:
        for i in puzzle:
            for j in i:
                al.append(str(j))
        coun = 0
        for i in d:
            d[i].set(al[coun])
            coun+=1
    



load = Image.open(r"bi.jpg")
si = ImageTk.PhotoImage(load)
sbutton = tk.Button(win,image = si,command = solve,bd = 0)
sbutton.place(x = 102,y=498)


win.mainloop()
