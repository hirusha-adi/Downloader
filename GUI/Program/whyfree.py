# #########################
# Made by ZeaCeR#5641
# a.k.a Hirusha Adikari
# #########################

# Imports - Main
# -----------------------
import sys

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
import whyfree_support

# Import - Other Windows
# -----------------------
import home



# Some more useful functions that support the GUI
# -----------------------
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    whyfree_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    whyfree_support.init(w, top, *args, **kwargs)
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

        top.geometry("604x450+794+247")
        top.minsize(117, 1)
        top.maxsize(4644, 1274)
        top.resizable(False,  False)
        top.title("Why Free?")
        top.configure(background="#ffffff")

        self.LMain = tk.Label(top)
        self.LMain.place(relx=0.0, rely=0.0, height=51, width=598)
        self.LMain.configure(background="#ffffff")
        self.LMain.configure(cursor="arrow")
        self.LMain.configure(disabledforeground="#a3a3a3")
        self.LMain.configure(font="-family {Showcard Gothic} -size 24")
        self.LMain.configure(foreground="#ff0f15")
        self.LMain.configure(text='''YouTube Video Downloader''')

        self.LMain_1 = tk.Label(top)
        self.LMain_1.place(relx=0.017, rely=0.178, height=41, width=125)
        self.LMain_1.configure(activebackground="#f9f9f9")
        self.LMain_1.configure(activeforeground="black")
        self.LMain_1.configure(background="#ffffff")
        self.LMain_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1.configure(font="-family {Sitka Display} -size 20")
        self.LMain_1.configure(foreground="#ff0f15")
        self.LMain_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1.configure(highlightcolor="black")
        self.LMain_1.configure(text='''Why Free?''')

        self.LMain_1_1 = tk.Label(top)
        self.LMain_1_1.place(relx=0.033, rely=0.289, height=21, width=477)
        self.LMain_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1.configure(activeforeground="black")
        self.LMain_1_1.configure(background="#ffffff")
        self.LMain_1_1.configure(cursor="arrow")
        self.LMain_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1.configure(highlightcolor="black")
        self.LMain_1_1.configure(text='''Once, i tried to download my music playlist to listen locally''')

        self.LMain_1_1_1 = tk.Label(top)
        self.LMain_1_1_1.place(relx=0.033, rely=0.356, height=21, width=487)
        self.LMain_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1.configure(text='''and the experience was inferior! The only options I had was''')

        self.LMain_1_1_1_1 = tk.Label(top)
        self.LMain_1_1_1_1.place(relx=0.033, rely=0.422, height=21, width=497)
        self.LMain_1_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1_1.configure(anchor='w')
        self.LMain_1_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1_1.configure(text='''to pay 40 USD to purchase that piece of software.... and YES!''')

        self.LMain_1_1_1_1_1 = tk.Label(top)
        self.LMain_1_1_1_1_1.place(relx=0.033, rely=0.489, height=21, width=497)
        self.LMain_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1_1_1.configure(anchor='w')
        self.LMain_1_1_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1_1_1.configure(text='''I didn't do it. I had a great idea of creating''')

        self.LMain_1_1_1_1_1_1 = tk.Label(top)
        self.LMain_1_1_1_1_1_1.place(relx=0.033, rely=0.556, height=21
                , width=497)
        self.LMain_1_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1_1_1_1.configure(anchor='w')
        self.LMain_1_1_1_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1_1_1_1.configure(text='''a YouTube Video Downloader myself, free and open source!''')

        self.LMain_1_1_1_1_1_1_1 = tk.Label(top)
        self.LMain_1_1_1_1_1_1_1.place(relx=0.033, rely=0.622, height=31
                , width=527)
        self.LMain_1_1_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1_1_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1_1_1_1_1.configure(anchor='w')
        self.LMain_1_1_1_1_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1_1_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1_1_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1_1_1_1_1.configure(text='''This is not a game changer.. but will get the work done''')

        self.LMain_1_1_1_1_1_1_1_1 = tk.Label(top)
        self.LMain_1_1_1_1_1_1_1_1.place(relx=0.679, rely=0.933, height=31
                , width=188)
        self.LMain_1_1_1_1_1_1_1_1.configure(activebackground="#f9f9f9")
        self.LMain_1_1_1_1_1_1_1_1.configure(activeforeground="black")
        self.LMain_1_1_1_1_1_1_1_1.configure(anchor='w')
        self.LMain_1_1_1_1_1_1_1_1.configure(background="#ffffff")
        self.LMain_1_1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.LMain_1_1_1_1_1_1_1_1.configure(font="-family {Sitka Display} -size 15")
        self.LMain_1_1_1_1_1_1_1_1.configure(foreground="#ff0f15")
        self.LMain_1_1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.LMain_1_1_1_1_1_1_1_1.configure(highlightcolor="black")
        self.LMain_1_1_1_1_1_1_1_1.configure(text='''Made by ZeaCeR#5641''')

        def go_to_home():
            top.destroy()
            home.vp_start_gui()

        self.gohome = tk.Button(top)
        self.gohome.place(relx=0.033, rely=0.733, height=84, width=567)
        self.gohome.configure(activebackground="#93ff51")
        self.gohome.configure(activeforeground="#000000")
        self.gohome.configure(background="#fc5c61")
        self.gohome.configure(disabledforeground="#a3a3a3")
        self.gohome.configure(font="-family {Uniflex_PersonalUseOnly} -size 24")
        self.gohome.configure(foreground="#000000")
        self.gohome.configure(highlightbackground="#d9d9d9")
        self.gohome.configure(highlightcolor="black")
        self.gohome.configure(pady="0")
        self.gohome.configure(text='''Go back to Home''')
        self.gohome.configure(command=go_to_home)

# if __name__ == '__main__':
#     vp_start_gui()





