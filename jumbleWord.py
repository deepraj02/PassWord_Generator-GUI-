
from tkinter import *
import tkinter.messagebox as tmsg
import random
from random import shuffle

#^ <============== List of Words ==================>

answers = ["america", "india", "australia", "deepraj",'klaus','dark','witcher'
           ,'originals','superman','thor','transformers','damon','stefan','vervain','werewolf']
questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions)-1)

#& Toggle Dark Mode

is_on = True


#* --------------------------- Backend ----------------------------------

  
# Define our switch function
def switch():
    global is_on
      
    # Determin is on or off
    if is_on:
        on_button.config(image = off)
        f.configure(background="#D1D1EC")
        lb1.configure(fg="#2C3335",bg="#D1D1EC")
        is_on = False
    else:
        
        on_button.config(image = on)
        f.config(background = '#2C3335')
        lb1.configure(fg="#D1D1EC",bg="#2C3335")
        is_on = True
  
# Define Our Images

def initial():
    global questions, num
    lb1.configure(text=questions[num])


def resetswitch():
    global questions, answers, num
    num = random.randint(0, len(questions)-1)
    lb1.configure(text=questions[num])
    e1.delete(0,END)

def answercheck():
    global questions, num, answers
    userinput = e1.get()
    if userinput == answers[num]:
        tmsg.showinfo('Success','You Guessed it Right')
        resetswitch()
    elif userinput==None:
        tmsg.showinfo('Error','Please Enter The Answer')
    else:
        tmsg.showinfo('Error','Your answer is wrong\n Guess it Again')
        e1.delete(0,END)


#% <------------------------ Main UI Body ------------------------------>

root = Tk()
root.geometry("400x449")
# root.configure(background='#2C3335')
root.title("JumbleWord Game")
root.iconbitmap(r"mainicon.ico")


on = PhotoImage(file = "Assets\on.png")
off = PhotoImage(file = "Assets\off.png")
  
# Create A Button
f=Frame(root)
f.pack(fill=BOTH)
l=Label(f,text="Toggle Dark Mode 👇",font="Firacode 8")
l.pack(pady=0)
on_button = Button(f, image = on, bd = 3,
                   command = switch)
on_button.pack(pady = 50)

lb1 = Label(f, font='Hack 20')
lb1.pack(pady=10, ipady=10, ipadx=10, fill=BOTH)

answer = StringVar()
e1 = Entry(f, textvariable=answer, font="Firacode 15")
e1.pack(ipady=5, ipadx=5)

button1 = Button(f, text="Check", bg='#75DA8B',
                 width=20, command=answercheck)
button1.pack(pady=45)

button3 = Button(f, text="Change Word", bg="#75DA8B",
                 width=20, command=resetswitch)
button3.pack(pady=10)



initial()
root.mainloop()