# #########################
# Made by ZeaCeR#5641
# a.k.a Hirusha Adikari
# #########################

# Imports - Main
# -----------------------
import sys, os
from PIL import ImageTk,Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

# Import - Support
# -----------------------
import credits_support
import credits_image

# Import - Other Windows
# -----------------------
import home



# Some more useful functions that support the GUI
# -----------------------
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    try:
        global val, w, root
        root = tk.Tk()
        top = Toplevel1 (root)
        credits_support.init(root, top)
        root.mainloop()
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            os.remove("temp_credits.png")
        except:
            try:
                os.system("rm temp_credits.png")
            except:
                pass

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    credits_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


# The GUI
# -----------------------
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+781+221")
        top.minsize(117, 1)
        top.maxsize(4644, 1274)
        top.resizable(False,  False)
        top.title("Credits")
        top.configure(background="#ffffff")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#ffffff',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.017, rely=0.022, height=51, width=594)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Showcard Gothic} -size 24")
        self.Label1.configure(foreground="#ff0f15")
        self.Label1.configure(text='''Credits''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.333, rely=0.711, height=31, width=204)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14")
        self.Label2.configure(foreground="#ff151c")
        self.Label2.configure(text='''Made by ZeaCeR#5641''')

        # Go back the Home Page
        # -----------------------
        def go_back_to_home():
            top.destroy()
            home.vp_start_gui()

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.033, rely=0.8, height=74, width=557)
        self.Button1.configure(activebackground="#41fe6b")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff5559")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Uniflex_PersonalUseOnly} -size 24")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Go back to Home''')
        self.Button1.configure(command=go_back_to_home)

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.3, rely=0.156, relheight=0.544, relwidth=0.408)

        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")
        # Setting the Image
        # -----------------------
        try:
            self.img = ImageTk.PhotoImage(Image.open("temp_credits.png"))
        except:
            credits_image.CREATE_CREDITS_IMG()
            self.img = ImageTk.PhotoImage(Image.open("temp_credits.png"))

        self.Canvas1.create_image(-20, -20, anchor=tk.NW, image=self.img)


# if __name__ == '__main__':
#     vp_start_gui()





