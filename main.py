
# Modules needed
from tkinter import *
import tkinter.messagebox as tmsb
import random
from PIL import Image, ImageTk

low = "abcdefghijklmnopqrstuvwxyz"
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sym = "[]{}()!@#-$%^&:;*_,.+=""<>~`"

main = (low+upp+num+sym)
root = Tk()
root.wm_iconbitmap("passman.ico")
root.title("Password-Generator")
root.geometry("600x460")

scvalue = StringVar()
scvalue.set('')

# ^ Functions
''' Need someone who can help me with this..'''


def sh():
    pass


def med():
    pass


def srt():
    pass


def cle():
    scvalue.set("")
    screen.update()


def qui():
    sure = tmsb.askquestion(
        "Confirm Exit", "Are you Sure You want to Exit\n???")
    if sure == "yes":
        quit()
#! Main body





# @ Heading
f1 = Frame(root, bg="#FF5733", borderwidth=10,relief=SUNKEN,)
he = Label(f1, text="Password-Generator", font="hack 30 bold").pack(anchor=N)
f1.pack(padx=2, pady=10)

screen = Entry(root, font="consolas 20")
screen.pack(side=LEFT, padx=10, pady=12, ipady=12, fill=BOTH, anchor=N)


# %Buttons.

b = Button(root, text="Strong", font="Consolas 18",
           bg="#0DEC76", width=10, command=srt)
b.pack(padx=10, pady=10, anchor=NE)
b = Button(root, text="Medium", font="Consolas 18",
           bg="#0DEC76", width=10, command=med)
b.pack(padx=10, pady=10, anchor=NE)

b = Button(root, text="Weak", font="Consolas 18",
           bg="#0DEC76", width=10, command=sh)
b.pack(padx=10, pady=10, anchor=NE)

b = Button(root, text="Clear", font="Consolas 18",
           bg="#0DEC76", width=10, command=cle)
b.pack(padx=10, pady=10, anchor=NE)

b = Button(root, text="Exit", font="Consolas 18",
           bg="#0DEC76", width=10, command=qui)
b.pack(padx=10, pady=10, anchor=NE)

root.mainloop()
