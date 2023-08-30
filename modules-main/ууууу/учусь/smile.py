from tkinter import *

import requests
import random
import time
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image, ImageTk

window = Tk()
window.geometry('900x630')
window.title('Улыбнись!')

points = 0


def world():
    clear()
    per = requests.get('https://fishki.net/2022785-25-chudes-rossii-kotorye-sotvorila-priroda.html')
    per = per.content

    soup = BeautifulSoup(per, 'lxml')
    w = random.choice(soup.find_all(loading="lazy"))
    w = w.get('src')
    rpic = requests.get(w)
    image = ImageTk.PhotoImage(Image.open(BytesIO(rpic.content)))

    label = Label(image=image)
    label.image = image
    label.place(x=10, y=10)
    draw_home_button()


def clicc():
    def check():
        global points
        but.place(x=random.randint(1, 800), y=random.randint(1, 570))
        points += 1
        label['text'] = points
        color = ['red', 'blue', 'purple', 'green', 'orange', 'yellow']
        if points % 10 == 0:
            but['fg'] = random.choice(color)
            time.sleep(2.0)
    points = 0
    clear()
    but = Button(text='Нажми меня', font=('Arial', 20), fg='black', command=check)
    but.place(x=200, y=130)
    label = Label(text=points, font=('Arial', 20), fg='red')
    label.place(x=10, y=10)


def cute():
    clear()
    per = requests.get('https://fonwall.ru/search?q=котята')
    per = per.content

    soup = BeautifulSoup(per, 'lxml')
    cat = random.choice(soup.find_all(class_='photo-item__img'))
    cat = cat.get('src')
    rcat = requests.get(cat)
    image = ImageTk.PhotoImage(Image.open(BytesIO(rcat.content)))

    label = Label(image=image)
    label.image = image
    label.place(x=30, y=30)


def phr():
    clear()
    per = requests.get('https://wikiphile.ru/570-fraz-o-motivacii/')
    per = per.content
    soup = BeautifulSoup(per, 'lxml')
    phr = random.choice(soup.find_all('li'))
    mes = Message(text=phr.text, font=('Arial', 20), fg='purple', width=880)
    mes.place(x=10, y=50)
    rcatt = requests.get('https://i.pinimg.com/originals/27/29/13/27291300c050e3d14d16f38b6d475fd6.jpg')
    image = ImageTk.PhotoImage(Image.open(BytesIO(rcatt.content)).resize((290, 290), Image.Resampling.LANCZOS))
    label = Label(image=image)
    label.image = image
    label.place(x=283, y=310)


def draw_menu():
    clear()
    Label_title = Label(text='Ты зачем грустишь? Как мне тебя развеселить?', font=('Arial', 26), fg='purple')
    Label_title.place(width=900, height=100, x=0, y=0)

    cats = Button(text='Увидеть котиков', font=('Arial', 20), fg='red', command=cute)
    cats.place(x=160, y=150)

    phrase = Button(text='Получить мотивацию', font=('Arial', 20), fg='green', command=phr)
    phrase.place(x=440, y=150)

    play = Button(text='Посмотреть мир', font=('Arial', 20), fg='blue', command=world)
    play.place(x=50, y=290)

    clic = Button(text='Поиграть в кликер', font=('Arial', 20), fg='orange', command=clicc)
    clic.place(x=580, y=290)

    rcatt = requests.get('https://i.pinimg.com/originals/27/29/13/27291300c050e3d14d16f38b6d475fd6.jpg')
    image = ImageTk.PhotoImage(Image.open(BytesIO(rcatt.content)).resize((290, 290), Image.Resampling.LANCZOS))
    label = Label(image=image)
    label.image = image
    label.place(x=283, y=310)


def clear():
    all_widgets = window.place_slaves()
    for l in all_widgets:
        l.destroy()
    draw_home_button()


def draw_home_button():
    home = Button(text='Меню', font=('Arial', 20), fg='green', command=draw_menu)
    home.place(x=800, y=570)


draw_menu()


window.mainloop()