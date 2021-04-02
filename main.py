
#* Modules needed

from tkinter import *
import tkinter.messagebox as tmsb
import random
from ttkthemes import themed_tk as t
from tkinter import ttk

root = t.ThemedTk(theme="ubuntu")
root.wm_iconbitmap("passman.ico")
root.geometry("540x370")
root.title("Password-Generator")
root.configure(bg="#2C3335")

#@ Heading 
f1 = Frame(root, bg="#FF5733", borderwidth=10,relief=SUNKEN)
he = Label(f1, text="Password-Generator", font="hack 30 bold").pack(anchor=N)
f1.pack(padx=2, pady=10)

screen = Entry(root, font="consolas 20",width=25)
screen.pack(side=LEFT, padx=10, pady=10, ipady=7, fill=BOTH, anchor=N)

# ^ Functions
def PassGen(n):
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    sym = "[]{}()!@#-$%^&:;*_,.+=""<>~`"
    main=(low+upp+num+sym)
    password="".join(random.sample(main,n))
    screen.delete(0,"end")
    screen.insert(0,password)

def cle():
    screen.delete(0,"end")

# %Buttons.
s = ttk.Style().configure('my.TButton', font="hack 14")


ttk.Button(root, text="Strong", style="my.TButton", width=10, command=lambda:PassGen(20)).pack(padx=10, pady=10, anchor=NE)
ttk.Button(root, text="Medium", style="my.TButton",width=10, command=lambda:PassGen(16)).pack(padx=10, pady=10, anchor=NE)

ttk.Button(root, text="Weak", style="my.TButton",width=10,command=lambda:PassGen(8)).pack(padx=10, pady=10, anchor=NE)

ttk.Button(root, text="Clear", style="my.TButton", width=10, command=cle).pack(padx=10, pady=10, anchor=NE)
root.mainloop()
