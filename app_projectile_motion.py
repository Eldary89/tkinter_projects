from tkinter import *
import math
import time

window = Tk()
window.title("Projectile motion app")
x = 0
y = 0
x1 = 40
y1 = 430
w = 20
speed = StringVar()
angle = StringVar()


def start_move(event):
    global x1, y1, w
    t = 0
    x = 0
    y = 0
    mx = 0
    g = 10
    v0 = float(speed.get())
    a0 = math.radians(float(angle.get()))
    tmax = (2 * v0 * math.sin(a0))/g
    while t < tmax:
        y = v0 * math.sin(a0) * t - 0.5 * g * t * t
        x = v0 * math.cos(a0) * t
        if mx < y:
            mx = y
        xy = x1 + x , y1 - y, x1 + x + w, y1 - y + w
        cnv.coords(oval,xy)
        window.update()
        time.sleep(0.01)
        t = t + 0.1
    cnv.coords(txt, 400, 100)
    cnv.itemconfig(txt, text = "Flight time is:"+str(int(t))+"\n"+"Total distance is:"+str(int(x))+"\n"+"Max height:"+str(int(mx)))


cnv = Canvas(window, width = 800, height = 500)
speed_entry = Entry(window, textvariable = speed)
angle_entry = Entry(window, textvariable = angle)
speed.set("Enter here a speed")
angle.set("Enter hera an angle")
cnv.pack()
speed_entry.pack()
angle_entry.pack()

cnv.create_line(0, 450, 800, 450)
cnv.create_line(50, 0, 50, 800)
for i in range(16):
    cnv.create_line(x, 440, x, 460)
    x = x + 50

for i in range(12):
    cnv.create_line(40, y, 60, y)
    y = y + 50

xy = x1, y1, x1 + w, y1 + w
oval = cnv.create_oval(xy, fill = "blue")
txt = cnv.create_text(0, 0, text = "")

window.bind("<Return>", start_move)
window.mainloop()