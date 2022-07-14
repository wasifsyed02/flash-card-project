from cgitb import text
from textwrap import fill
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word_dict={}
data={}
try:
    orginal_data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_to_learn=pandas.read_csv("data/french_words.csv")
    data=word_to_learn.to_dict(orient="records")

else:
    data=orginal_data.to_dict(orient="records")



def next_card():
    global word_dict,flip_timer
    window.after_cancel(flip_timer)
    word_dict=random.choice(data)
    french_word=word_dict["French"]
    canvas.itemconfig(bg_image,image=front_image)
    canvas.itemconfig(lang_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=french_word,fill="black")
    flip_timer=window.after(3000,flip_card)
def flip_card():
    english_word=word_dict["English"]
    canvas.itemconfig(lang_text,text="English",fill="white")
    canvas.itemconfig(bg_image,image=back_image)
    canvas.itemconfig(word_text,text=english_word,fill="white")
def is_known():
    data.remove(word_dict)
    words_to_learn=pandas.DataFrame(data)
    words_to_learn.to_csv("data/words_to_learn.csv",index=False)
    next_card()


from tkinter import *
from turtle import bgcolor, bgpic, title
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash scard Game.")
flip_timer=window.after(3000,flip_card)
canvas=Canvas(width=800,height=526)
front_image=PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
bg_image=canvas.create_image(400,256,image=front_image)
lang_text=canvas.create_text(400,154,text="French",font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,264,text="English",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
wrong_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)
right_image=PhotoImage(file="images/right.png")
known_button=Button(image=right_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)
next_card()
window.mainloop()
