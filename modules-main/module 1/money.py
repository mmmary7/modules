# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
# #date = "date_req=26/01/2023"
# today = datetime.today()
# today = today.strftime('%d/%m/%Y')
# date = {'date_req' : today}
#
# responce = requests.get(url, params=date)
# xml = BeautifulSoup(responce.content, 'lxml')
#
#
# def getCourse(id):
#     course = xml.find('valute', {'id':id}).value.text
#     return course
#
#
# def nom(id):
#     nominal = xml.find('valute', {'id': id}).nominal.text
#     return nominal
#
#
#
# print(getCourse('R01280'), 'рублей за', nom('R01280'), 'индонезейских рупий')
from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# window = Tk()
# window.title('Форточка')
# window.geometry('500x500+100+100')
# count = 0
# def change_count():
#     global count
#     count += 1
#     lab['text'] = str(count)
#
# lab = Label(window, text='Красивый вид', bg='red', fg='#555', font=16)
# lab.place(height=30, width=150, x=100, y=100)
#
# btn = Button(text='Нажми меня', bg='yellow', fg='#131313', font='16', command=change_count)
# btn.place(x=100, y=200)
# window.mainloop()
window = Tk()
window.geometry('600x300+300+300')
window.title('Курс валют')
window.resizable(width=False, height=False)

today = datetime.today()
today = today.strftime('%d/%m/%Y')
playload = {'data_req': today}

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params=playload)
xml = BeautifulSoup(responce.content, features="xml")


def get_course(id):
    return xml.find('Valute', {'ID': id}).Value.text


img = PhotoImage(file='logo.png')
logo = Label(window, image=img)
logo.place(x=0, y=0)

lab = Label(window, text='Курс валют \n от банка Код будущего', font='Arial 18', bg='#00FFFF', fg='#FFFFFF')
lab.place(y=20, x=280)

cource_info = Label(window, text='Курс валют на: '+today.replace('/', '.'), font='Arial, 15', bg='#00FF00')
cource_info.place(x=300, y=230)

usd_course = Label(window, text='$'+get_course('R01235'), font='Arial 16', bg='#FFFF00', fg='#FF1493')
usd_course.place(x=360, y=100)

euro_course = Label(window, text='€'+get_course('R01239'), font='Arial 16', bg='#FFF200', fg='#9400D3')
euro_course.place(x=360, y=140)

yuan_course = Label(window, text='¥'+get_course('R01375'), font='Arial 16', bg='#FFD700', fg='#8A2BE2')
yuan_course.place(x=360, y=180)

window.mainloop()