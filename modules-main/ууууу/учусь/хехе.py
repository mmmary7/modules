
from tkinter import *

window = Tk()
window.geometry('700x500')
window.title('Тест по мультику "Леди баг и Супер кот"')

label_title = Label(text="Тестирование по мультику",
                    font=('Arial', 24), fg='white', bg='red')
label_title.place(width=700, height=50, x=0, y=0)

facts = [
    {'text': 'Маринетт влюбилась в Эдриана как только увидела его',
     'right': 0},
    {'text': 'Леди баг не только супергероиня, но и хранительница талисманов',
     'right': 1},
    {'text': 'Квами пчелы зовут Поллен',
     'right': 1},
    {'text': 'Камень чудес кота был только у Эдриана',
     'right': 0},
    {'text': 'Режиссёр мультсериала - Томас Астрюк',
     'right': 1}
]
cur_q = 0
points = 0


def check():
    global cur_q, points
    answer = var.get()
    if answer == facts[cur_q]['right']:
        points += 1
    if cur_q < len(facts) - 1:
        cur_q += 1
        fact['text'] = facts[cur_q]['text']
    else:
        points_label = Label(text='Вы набрали ' + str(points) + ' очка',
                             font=('Arial', 30), fg='white', bg='red')
        points_label.place(x=0, y=0, width=700, height=250)
        if points >= len(facts)/2:
            label_happy.place(x=0, y=250, width=700, height=250)
        else:
            label_sad.place(x=0, y=250, width=700, height=250)


fact = Message(text=facts[cur_q]['text'], font=('Arial', 14),
               width=680, borderwidth=0)
fact.configure(justify=CENTER)
fact.place(x=10, y=70)
var = IntVar()
false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=170)
true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=120)
b = Button(text='Ответить', font=('Arial', 20), fg='black', command=check)
b.place(x=200, y=130)

pic_happy = PhotoImage(file='happy.png')
label_happy = Label(image=pic_happy)

pic_sad = PhotoImage(file='sad.png')
label_sad = Label(image=pic_sad)

window.mainloop()
