from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("786x518")
window.configure(bg = "#e3ffdc")
canvas = Canvas(
    window,
    bg = "#e3ffdc",
    height = 518,
    width = 786,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    324.5, 272.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    326.5, 172.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 122.0, y = 146,
    width = 409.0,
    height = 51)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 221, y = 424,
    width = 343,
    height = 73)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 564, y = 146,
    width = 123,
    height = 53)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 697, y = 146,
    width = 53,
    height = 53)

window.resizable(False, False)
window.mainloop()
