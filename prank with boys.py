from tkinter import *
from tkinter import messagebox
import random

que = ['Are you gay?', 'Are you playboy?', 'Are you Chapri?', 'Are you Trance gender?', 'Have you ever seen him play a musical instrument?',
'Does he enjoy watching sports?', 'Has he ever traveled outside the country?', 'Does he have a pet?', 'Is he a fan of science fiction movies?',
'Is he good at cooking?', 'Does he have any siblings?', 'Is he a night owl?', 'Has he ever been in a long-distance relationship?',
'Is he a fan of video games?', 'Does he like spicy food?', 'Is he a bookworm?', 'Does he have a favorite superhero?',
'Is he tech-savvy?', 'Does he prefer beaches over mountains?', 'Has he ever gone camping in the wilderness?' ]

def no():
    messagebox.showinfo(' ', 'Thanks You for honiste')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0,500), y= random.randint(0, 500))

root = Tk()
root.geometry('500x500')
root.title('Only Truth')
root['bg'] = 'black'

# Label = Label(root, text='Are you chapri?' , font='Arial 20 bold', bg='white')
Label = Label(root, text=random.choice(que) , font='Arial 20 bold', bg='white')
Label.pack()

btnYes = Button (root, text='No' , font='Arial 20 bold')
btnYes.place(x=150, y=100)
btnYes.bind('<Enter>',motionMouse)

btnNo = Button (root, text='Yes' , font='Arial 20 bold', command=no)
btnNo.place(x=300, y=100)

root.mainloop()