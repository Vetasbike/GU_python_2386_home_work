"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
— на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from tkinter import *
import time


class TrafficLight(Tk):

    def __init__(self):
        self.count = 0
        super().__init__()
        self.title('Светофор')
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")
        self.r = c.create_oval(10, 10, 60, 60, fill="#ff0000")
        self.y = c.create_oval(10, 70, 60, 120, fill="#808000")
        self.g = c.create_oval(10, 130, 60, 180, fill="#008000")
        c.pack()
        self.update()
        self.after(7000, self.running)

    def running(self):
        if self.count == 0:
            self.count = 1
            self.canvas.itemconfigure(self.r, fill='#800000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(2000, self.running)
        elif self.count == 1:
            self.count = 2
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(2000, self.running)
        elif self.count == 2:
            self.count = 3
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.canvas.itemconfigure(self.r, fill='#800000')
            self.after(750, self.running)
        else:
            self.count = 0
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.after(7000, self.running)

root = TrafficLight()
root.mainloop()
