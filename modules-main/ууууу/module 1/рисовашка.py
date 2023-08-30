from tkinter import *

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

canvas.create_rectangle(10, 10, 70, 70, fill='yellow', outline='blue')
canvas.create_rectangle(10, 10, 50, 50, fill='red', outline='blue')
canvas.create_rectangle(10, 10, 30, 30, fill='yellow', outline='blue')


canvas.create_rectangle(100, 100, 180, 180, fill='brown')
canvas.create_rectangle(120, 120, 160, 160, fill='blue')
canvas.create_polygon(100, 100, 140, 60, 180, 100, fill='purple')


window.mainloop()
