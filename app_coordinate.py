from tkinter import *
import time
import math

window = Tk()
window.geometry("800x600")
window.title("Coordinate app")

cnv = Canvas(window)
cnv.pack(fill = BOTH, expand = 1)

x = 0
y = 0

x1 = 45
y1 = 295
w = 10

x11 = 50
y11 = 300


def start_move(event):
    x = 0
    while x < 700:
        x = x + 10
        y = 50 * (math.sin(x/50))
        xy = x1 + x, y1 - y, x1 + x + w, y1 - y + w
        cnv.coords(oval, xy)
        cnv.create_line(x11 + x - 10, y11 - 50 * (math.sin((x-10)/50)), x11 + x, y11 - y)
        window.update()
        print("y:"+str(y))
        time.sleep(0.02)


cnv.create_line(0, 300, 800, 300)
cnv.create_line(50, 0, 50, 600)
for i in range(16):
    cnv.create_line(x, 290, x, 310)
    x = x + 50

for i in range(12):
    cnv.create_line(40, y, 60, y)
    y = y + 50

oval = cnv.create_oval(x1, y1, x1+w, y1+w, fill="red")

window.bind("<Return>", start_move)

window.mainloop()