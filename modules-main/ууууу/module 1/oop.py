from tkinter import *

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()
# class Car:
#     def __init__(self):
#         print("я родился")
#     def bibicar(self):
#         print("bi bi bi")

class House:
    def __init__(self, roof_color, wall_color, number):
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.number = number
        self.height = 130
        self.width = 140
        self.wall = None
        self.roof = None

    def build(self, x, y):
        w = self.width
        h = self.height

        self.roof = canvas.create_polygon(x, y, x+w, y, x+w/2, h-100, fill=self.roof_color)
        self.wall = canvas.create_rectangle(x+20, y, x+120, y+100, fill=self.wall_color)

    def info_house(self):
        print(f'цвет дома {self.wall_color} \nцвет крыши {self.roof_color} \nномер дома {self.number}')


house_1 = House("green", "yellow", 1)
house_1.build(100, 100)

house_1.info_house()

window.mainloop()