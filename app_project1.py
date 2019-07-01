from tkinter import *
from tkinter import colorchooser

window = Tk()
color = (0, "Red")
shape = "R"


def draw_shape(event):
    global shape
    w = width_scale.get()
    h = height_scale.get()
    xy = event.x - w/2, event.y - h/2, event.x+w/2, event.y+h/2
    if shape == "R":
        cnv.create_rectangle(xy, fill = color[1])
    elif shape == "O":
        cnv.create_oval(xy, fill = color[1])
    elif shape == "L":
        cnv.create_line(xy, fill = color[1])


def choose_rectangle():
    global shape
    shape = "R"


def choose_oval():
    global shape
    shape = "O"


def choose_line():
    global shape
    shape = "L"


def choose_color():
    global color
    color = colorchooser.askcolor("Red")
    print(color)


toolbarPane = Frame(window)
canvasPane = Frame(window, relief = RAISED, bd = 3, cursor = "cross")
toolbarPane.pack(side = LEFT)
canvasPane.pack()


cnv = Canvas(canvasPane, width = 500, height = 600)
cnv.pack()

rec_but = Button(toolbarPane, text = "Rectangle", width = 15, command = choose_rectangle)
oval_but = Button(toolbarPane, text = "Oval", width = 15, command = choose_oval)
line_but = Button(toolbarPane, text = "Line", width = 15, command = choose_line)
color_but = Button(toolbarPane, text = "Color", width = 15, command = choose_color)
height_lbl = Label(toolbarPane, text = "Height", width = 15)
height_scale = Scale(toolbarPane, from_=0, to = 500, width = 15, orient = HORIZONTAL)
width_lbl = Label(toolbarPane, text = "Width", width = 15)
width_scale = Scale(toolbarPane, from_=0, to = 500, width = 15, orient = HORIZONTAL)

rec_but.pack()
oval_but.pack()
line_but.pack()
color_but.pack()
height_lbl.pack()
height_scale.pack()
width_lbl.pack()
width_scale.pack()

cnv.bind("<Button-1>", draw_shape)

window.mainloop()