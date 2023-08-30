from tkinter import *
import random

window = Tk()
w = 600
h = 600
window.geometry(str(w)+"x"+str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file='bg_2.png')


class Knight:
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.v = 0
        self.photo = PhotoImage(file='knight.png')
    def up(self, event):
        self.v += -3
    def down(self, event):
        self.v += 3
    def stop(self, event):
        self.v = 0


class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(3, 5)
        self.photo = PhotoImage(file='dragon.png')


knight = Knight()
dragons = []
for i in range(5):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(h//2, w//2, image=bg_photo)
    # if 60 <= knight.y <= 540:
    knight.y += knight.v
    # if 55 <= knight.y <= 65:
    #     knight.y += 300
    # if knight.y == 540 or knight.y == 541 or knight.y == 542:
    #     knight.y = 539
    canvas.create_image(knight.x, knight.y, image=knight.photo)

    current_dragon = 0
    dragon_to_kill = -1
    for dragon in dragons:
        dragon.x += -dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        if (dragon.x - knight.x)**2+(dragon.y-knight.y)**2 < 96**2:
            dragon_to_kill = current_dragon
        current_dragon += 1
        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text='YOU LOSE! :(', font='Verdana 42', fill='red')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]
    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text='YOU WIN! :)', font='Verdana 42', fill='red')
    else:
        window.after(20, game)


window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)

game()

window.mainloop()

