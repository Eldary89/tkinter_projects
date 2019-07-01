from tkinter import *
import time
import math

window = Tk()
window.title("Coordinate app")

k = StringVar()

cnv = Canvas(window, width=800, height=600)
cnv.pack()
k_entry = Entry(window, textvariable=k)
k.set("Enter the k parameter")
k_entry.pack()

x = 0
y = 0

# The properties of the ball
x1 = 45
y1 = 545
w = 10

# The properties of the line which will be drawn while the ball is moving
x11 = 50
y11 = 550


def start_move(event):
    x = 0
    k0 = float(k.get())
    while x < 600:
        xy = x1 + x, y1 - k0 * x, x1 + x + w, y1 - k0 * x + w
        cnv.coords(oval, xy)
        cnv.create_line(x11 + x, y11 - k0 * x, x11 + x + 10, y11 - k0 * (x + 10))
        window.update()
        time.sleep(0.02)
        x = x + 10


cnv.create_line(0, 550, 800, 550)
cnv.create_line(50, 0, 50, 600)
for i in range(16):
    cnv.create_line(x, 540, x, 560)
    x = x + 50

for i in range(12):
    cnv.create_line(40, y, 60, y)
    y = y + 50

oval = cnv.create_oval(x1, y1, x1 + w, y1 + w, fill="red")

window.bind("<Return>", start_move)

window.mainloop()
