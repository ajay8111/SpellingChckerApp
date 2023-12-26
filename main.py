import tkinter
from tkinter import *
from textblob import *

rt = Tk()
rt.title("Spelling Checker")
rt.geometry("700x400")
rt.config(background="#ffb6c1")

def check_spelling():
    word = enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs = Label(rt,text="Correct Spelling is :",font=("poppins",20),bg="#ffb6c1",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label(rt,text="Spelling Check", font=("Trebuchet MS",30,"bold"),bg="#ffb6c1",fg="#364971")
heading.pack(pady=(50,0))

enter_text = Entry(rt,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(rt,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()

spell = Label(rt,font=("poppins",20),bg="#ffb6c1",fg="#364971")
spell.place(x=350,y=250)
rt.mainloop()