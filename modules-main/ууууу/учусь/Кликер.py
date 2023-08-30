from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.title('Кликер')

points = 0


def check():
    global points
    b.place(x=random.randint(1, 550), y=random.randint(1, 350))
    points += 1
    label['text'] = points
    if points == 10:
        b['fg'] = 'red'
        time.sleep(2.0)


b = Button(text='Нажми меня', font=('Arial', 20), fg='black', command=check)
b.place(x=200, y=130)
label = Label(text=points, font=('Arial', 20), fg='red')
label.place(x=10, y=10)


window.mainloop()
