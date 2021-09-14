# #########################
# Made by ZeaCeR#5641
# a.k.a Hirusha Adikari
# For any issue, please contact me!
# #########################

from tkinter import *
from tkinter import messagebox
import webbrowser, os, images
# import homewindow


if "start.exe" in os.listdir(os.getcwd()) or "home.exe" in os.listdir(os.getcwd()):
    pass
else:
    try:
        if "background2.png" in os.listdir(f"{os.getcwd()}\\assets") and "background.png" in os.listdir(f"{os.getcwd()}\\assets"):
            pass
        else:
            images.CREATE_ALL_IMAGES()
    except:
        # print(e)
        images.CREATE_ALL_IMAGES()


# Tkinter window
# --------------------
creditswin = Tk()
creditswin.geometry("786x518")
creditswin.configure(bg = "#e3ffdc")
creditswin.resizable(False, False)
creditswin.title("Downloader - Credits")


# Functions
# --------------------
def RUN_HOME():
    try:
        os.system(".\home.exe")
    except:
        messagebox.showerror("Error!", "Unable to find credits.exe")


def window_credits():
    messagebox.showinfo("Credits", "You are already in the Credits window!")

def window_home_go():
    messagebox.showinfo("Credits", "You need to be in the Home window to do this")
    creditswin.destroy()
    RUN_HOME()

def window_home():
    creditswin.destroy()
    RUN_HOME()

def others_source_code():
    webbrowser.open("https://github.com/hirusha-adi/Downloader/")

def others_privacy_policy():
    webbrowser.open("https://github.com/hirusha-adi/Downloader/blob/main/privacy-policy.md")

def others_help():
    webbrowser.open("https://github.com/hirusha-adi/Downloader/blob/main/help.md")


# Canvas
# --------------------
canvas = Canvas(
    creditswin,
    bg = "#e3ffdc",
    height = 518,
    width = 786,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file="assets\\background2.png")
background = canvas.create_image(
    356.5, 257.5,
    image=background_img)

# MunBar
# --------------------
menubar = Menu(creditswin)
creditswin.configure(menu = menubar)

sub_menu = Menu(creditswin, tearoff=0)
menubar.add_cascade(menu=sub_menu, label="Main")
if "start.exe" in os.listdir(os.getcwd()) or "home.exe" in os.listdir(os.getcwd()):
    sub_menu.add_command(label="Download", command=window_home_go)
    sub_menu.add_command(label="Paste URL", command=window_home_go)
    sub_menu.add_command(label="Clear URL", command=window_home_go)
else:
    sub_menu.add_command(label="Download", command=window_home_go, state="disabled")
    sub_menu.add_command(label="Paste URL", command=window_home_go, state="disabled")
    sub_menu.add_command(label="Clear URL", command=window_home_go, state="disabled")

sub_menu.add_command(label="Exit", command=lambda: exit())

sub_menu_three = Menu(creditswin, tearoff=0)
menubar.add_cascade(menu=sub_menu_three, label="Windows")
if "start.exe" in os.listdir(os.getcwd()) or "home.exe" in os.listdir(os.getcwd()):
    sub_menu_three.add_command(label="Home", command=window_home)
else:
    sub_menu_three.add_command(label="Home", command=window_home, state="disabled")
sub_menu_three.add_command(label="Credits", command=window_credits)

sub_menu_two = Menu(creditswin, tearoff=0)
menubar.add_cascade(menu=sub_menu_two, label="Others")
sub_menu_two.add_command(label="Support Us", command=lambda: webbrowser.open("https://www.youtube.com/c/HirushaAdikari?sub_confirmation=1"))
sub_menu_two.add_command(label="Privacy Policy", command=others_privacy_policy)
sub_menu_two.add_command(label="Source Code", command=others_source_code)
sub_menu_two.add_command(label="Help", command=others_help)

# if "start.exe" in os.listdir(os.getcwd()) or "home.exe" in os.listdir(os.getcwd()):
#     pass
# else:
#     images.DELETE_ALL()



creditswin.mainloop()






